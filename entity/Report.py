# entity/Report.py

class Report:
    def __init__(self, report_id=None, incident_id=None, reporting_officer_id=None, report_date=None,
                 report_details=None, status=None):
        self.__report_id = report_id
        self.__incident_id = incident_id
        self.__reporting_officer_id = reporting_officer_id
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status

    # Getters
    def get_report_id(self):
        return self.__report_id

    def get_incident_id(self):
        return self.__incident_id

    def get_reporting_officer_id(self):
        return self.__reporting_officer_id

    def get_report_date(self):
        return self.__report_date

    def get_report_details(self):
        return self.__report_details

    def get_status(self):
        return self.__status

    # Setters
    def set_report_id(self, report_id):
        self.__report_id = report_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def set_reporting_officer_id(self, reporting_officer_id):
        self.__reporting_officer_id = reporting_officer_id

    def set_report_date(self, report_date):
        self.__report_date = report_date

    def set_report_details(self, report_details):
        self.__report_details = report_details

    def set_status(self, status):
        self.__status = status
