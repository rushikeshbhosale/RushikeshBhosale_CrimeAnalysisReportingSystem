from typing import List, Collection
from datetime import datetime
from entity.Incident import Incident
from entity.Cases import Case
from entity.Report import Report
from entity.IncidentType import IncidentType
from exception.MyExceptions import IncidentIDNotFoundException, IncidentTypeNotFoundException, CaseNotFoundException
from util.DBConnection import DBConnection


class CrimeAnalysisServiceImpl:
    connection = None

    def __init__(self):
        # Initialize the database connection
        self.connection = DBConnection.get_connection()

    def createIncident(self, incident: Incident) -> bool:
        try:
            # Check if the incident date is not in the future
            incident_date = datetime.strptime(incident.get_incident_date(), "%Y-%m-%d").date()
            if incident_date > datetime.now().date():
                raise ValueError("Incident date cannot be a future date.")

            # Validate incident type
            if not incident.get_incident_type().isalpha():
                raise ValueError("Incident type should only contain alphabetic characters.")

            # Validate incident description
            if not incident.get_description().replace(" ", "").isalpha():
                raise ValueError("Incident description should only contain alphabetic characters.")

            # Continue with the rest of the code for creating the incident
            cursor = self.connection.cursor()
            query = "INSERT INTO Incident (incident_type, incident_date, location_latitude, location_longitude, description, status, victim_id, suspect_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                incident.get_incident_type(), incident.get_incident_date(), incident.get_location_latitude(),
                incident.get_location_longitude(), incident.get_description(), incident.get_status(),
                incident.get_victim_id(), incident.get_suspect_id()))
            self.connection.commit()

            # Get the last inserted incident ID
            incident_id = cursor.lastrowid

            # Set the incident ID to the incident object
            incident.set_incident_id(incident_id)

            return True
        except ValueError as e:
            print(f"Error creating incident: {e}")
            return False

    def deleteIncidentById(self, incident_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Incident WHERE incident_id = %s"
            cursor.execute(query, (incident_id,))
            if cursor.rowcount == 0:
                raise IncidentIDNotFoundException(f"Incident with ID {incident_id} not found")
            # Reset auto-increment counter for Incident table
            self.reset_auto_increment("Incident")
            self.connection.commit()
            return True
        except IncidentIDNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error deleting incident: {e}")
            return False

    def reset_auto_increment(self, table_name: str):
        try:
            cursor = self.connection.cursor()
            query = f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;"
            cursor.execute(query)
            print(f"Auto-increment counter for table '{table_name}' reset successfully.")
        except Exception as e:
            print(f"Error resetting auto-increment counter: {e}")

    def updateIncidentStatus(self, status: str, incident_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Incident SET status = %s WHERE incident_id = %s"
            cursor.execute(query, (status, incident_id))
            if cursor.rowcount == 0:
                raise IncidentIDNotFoundException(
                    f"Incident with ID {incident_id} not found")  # Raise the custom exception
            self.connection.commit()
            return True
        except IncidentIDNotFoundException as e:
            # Re-raise the custom exception
            raise e
        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False

    def getIncidentsInDateRange(self, start_date, end_date) -> Collection[Incident]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incident WHERE incident_date BETWEEN %s AND %s"
            cursor.execute(query, (start_date, end_date))
            incidents = []
            for row in cursor.fetchall():
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                incidents.append(incident)
            return incidents
        except Exception as e:
            print(f"Error getting incidents in date range: {e}")
            return []

    def searchIncidents(self, criteria: IncidentType) -> Collection[Incident]:
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incident WHERE incident_type = %s"
        cursor.execute(query, (criteria.get_type_name(),))
        incidents = []
        for row in cursor.fetchall():
            incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            incidents.append(incident)
        if not incidents:
            raise IncidentTypeNotFoundException(f"Incident type '{criteria.get_type_name()}' not found")
        return incidents

    def generateIncidentReport(self, incident: Incident, reporting_officer_id: int, report_date: datetime,
                               status: str) -> Report:
        report = None
        try:
            # Validate report date
            if report_date > datetime.now().date():
                raise ValueError("Report date cannot be in the future.")

            cursor = self.connection.cursor()
            query = "INSERT INTO Report (incident_id, reporting_officer_id, report_date, report_details, status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (
                incident.get_incident_id(), reporting_officer_id, report_date, "Generated report details", status))
            self.connection.commit()

            # Create a new Report instance with auto-generated report_id and other details
            report = Report(None, incident.get_incident_id(), reporting_officer_id, report_date,
                            "Generated report details", status)
        except Exception as e:
            print(f"Error generating incident report: {e}")
        return report

    def createCase(self, case_description: str, case_status: str) -> Case:
        new_case = None
        try:
            cursor = self.connection.cursor()

            # Insert case description and case status into the Cases table
            query_insert_case = "INSERT INTO Cases (case_description, case_status) VALUES (%s, %s)"
            cursor.execute(query_insert_case, (case_description, case_status))
            case_id = cursor.lastrowid

            self.connection.commit()
            new_case = Case(case_id, case_description, case_status)
        except Exception as e:
            print(f"Error creating case: {e}")
        return new_case

    def getCaseDetails(self, case_id: int) -> Case:
        case_details = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Cases WHERE case_id = %s"
            cursor.execute(query, (case_id,))
            row = cursor.fetchone()
            if row:
                case_id = row[0]
                case_description = row[1]
                case_status = row[2]
                case_details = Case(case_id, case_description, case_status)
        except Exception as e:
            print(f"Error getting case details: {e}")
        return case_details

    def updateCaseDetails(self, case: Case) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Cases SET case_status = %s WHERE case_id = %s"
            cursor.execute(query, (case.get_case_status(), case.get_case_id()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    def getAllCases(self) -> List[Case]:
        all_cases = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Cases"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                case_id = row[0]
                case_description = row[1]
                case_status = row[2]
                all_cases.append(Case(case_id, case_description, case_status))
        except Exception as e:
            print(f"Error getting all cases: {e}")
        return all_cases

    def getIncidentById(self, incident_id: int) -> Incident:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incident WHERE incident_id = %s"
            cursor.execute(query, (incident_id,))
            row = cursor.fetchone()
            if row:
                return Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            else:
                return None
        except Exception as e:
            print(f"Error getting incident by ID: {e}")
            return None

    # Inside the getIncidentReport method in CrimeAnalysisServiceImpl class
    def getIncidentReport(self, incident_id: int) -> Report:
        try:
            cursor = self.connection.cursor()

            # Check if incident_id exists in the Incident table
            query_incident = "SELECT * FROM Incident WHERE incident_id = %s"
            cursor.execute(query_incident, (incident_id,))
            if cursor.fetchone() is None:
                raise ValueError(f"Incident with ID {incident_id} not found.")

            # Query for the report
            query = "SELECT * FROM Report WHERE incident_id = %s"
            cursor.execute(query, (incident_id,))
            row = cursor.fetchone()
            if row:
                # Create and return the report object
                report = Report(row[0], row[1], row[2], row[3], row[4], row[5])
                return report
            else:
                print(f"No report found for incident ID {incident_id}.")
                return None
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return None
        except Exception as e:
            print(f"Error getting incident report: {e}")
            return None

    def updateIncidentReportStatus(self, report_id: int, new_status: str) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Report SET status = %s WHERE report_id = %s"
            cursor.execute(query, (new_status, report_id))
            if cursor.rowcount == 0:
                return False
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating incident report status: {e}")
            return False

    def deleteIncidentReport(self, report_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Report WHERE report_id = %s"
            cursor.execute(query, (report_id,))
            if cursor.rowcount == 0:
                raise IncidentIDNotFoundException(f"Incident report with ID {report_id} not found.")
            self.connection.commit()
            # Reset auto-increment counter after successful deletion
            self.reset_auto_increment("Report")
            return True
        except Exception as e:
            return False

    def deleteCase(self, case_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Cases WHERE case_id = %s"
            cursor.execute(query, (case_id,))
            if cursor.rowcount == 0:
                raise CaseNotFoundException(f"Case with ID {case_id} not found.")
            self.connection.commit()

            # Reset auto-increment counter after successful deletion
            self.reset_auto_increment("Cases")

            return True
        except CaseNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error deleting case: {e}")
            return False
