import unittest
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incident import Incident
from entity.Cases import Case
from entity.IncidentType import IncidentType


class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        self.service = CrimeAnalysisServiceImpl()

    def test_create_incident(self):
        # Test createIncident method
        incident = Incident(None, "Theft", "2024-05-10", "12.345", "98.765", "Theft occurred", "Open", "1", "4")
        result = self.service.createIncident(incident)
        self.assertTrue(result)

        # assertions to check attributes of the created incident
        # Check if incident ID is assigned
        self.assertIsNotNone(incident.get_incident_id())
        # Check if incident type matches
        self.assertEqual(incident.get_incident_type(), "Theft")
        # Check if incident date matches
        self.assertEqual(incident.get_incident_date(), "2024-05-10")
        # Check if location latitude matches
        self.assertEqual(incident.get_location_latitude(), "12.345")
        # Check if location longitude matches
        self.assertEqual(incident.get_location_longitude(), "98.765")
        # Check if description matches
        self.assertEqual(incident.get_description(), "Theft occurred")
        # Check if status matches
        self.assertEqual(incident.get_status(), "Open")
        # Check if victim ID matches
        self.assertEqual(incident.get_victim_id(), "1")
        # Check if suspect ID matches
        self.assertEqual(incident.get_suspect_id(), "4")

    def test_update_incident_status(self):
        # Test updateIncidentStatus method
        incident_id = 1  # valid incident ID
        new_status = "Open"
        result = self.service.updateIncidentStatus(new_status, incident_id)
        self.assertTrue(result)
        # assertions to check if status is updated correctly
        # Check if the status is updated to the new status
        updated_incident = self.service.getIncidentById(incident_id)
        self.assertEqual(updated_incident.get_status(), new_status)

    def test_delete_incident_by_id(self):
        # Test deleteIncidentById method
        incident_id = 6  # Provide a valid incident ID
        result = self.service.deleteIncidentById(incident_id)
        self.assertTrue(result)

    def test_search_incidents(self):
        # Test searchIncidents method
        incident_type_name = "Theft"  # correct incident type name
        incident_type = IncidentType(type_name=incident_type_name)
        result = self.service.searchIncidents(incident_type)
        self.assertTrue(result)

    def test_create_case(self):
        # Test createCase method
        case_description = "Case description"
        case_status = "Draft"
        result = self.service.createCase(case_description, case_status)
        self.assertTrue(result)

    def test_get_case_details(self):
        # Test getCaseDetails method
        case_id = 1  # valid case ID
        result = self.service.getCaseDetails(case_id)
        self.assertTrue(result)

    def test_update_case_details(self):
        # Test updateCaseDetails method
        case = Case(1, "Case description", "Finalized")
        result = self.service.updateCaseDetails(case)
        self.assertTrue(result)

    def test_get_all_cases(self):
        # Test getAllCases method
        result = self.service.getAllCases()
        self.assertTrue(result)

    def test_get_incident_by_id(self):
        # Test getIncidentById method
        incident_id = 1  # valid incident ID
        result = self.service.getIncidentById(incident_id)
        self.assertTrue(result)

    def test_get_incident_report(self):
        # Test getIncidentReport method
        incident_id = 1  # valid incident ID
        result = self.service.getIncidentReport(incident_id)
        self.assertTrue(result)

    def test_delete_incident_report(self):
        # Test deleteIncidentReport method
        report_id = 2  # valid report ID
        result = self.service.deleteIncidentReport(report_id)
        self.assertTrue(result)

    def test_delete_case(self):
        # Test deleteCase method
        case_id = 4  # valid case ID
        result = self.service.deleteCase(case_id)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

