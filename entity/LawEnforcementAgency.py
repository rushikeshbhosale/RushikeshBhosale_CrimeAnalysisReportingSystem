# entity/LawEnforcementAgency.py

class LawEnforcementAgency:
    def __init__(self, agency_id=None, agency_name=None, jurisdiction=None, contact_information=None):
        self.__agency_id = agency_id
        self.__agency_name = agency_name
        self.__jurisdiction = jurisdiction
        self.__contact_information = contact_information

    # Getters
    def get_agency_id(self):
        return self.__agency_id

    def get_agency_name(self):
        return self.__agency_name

    def get_jurisdiction(self):
        return self.__jurisdiction

    def get_contact_information(self):
        return self.__contact_information

    # Setters
    def set_agency_id(self, agency_id):
        self.__agency_id = agency_id

    def set_agency_name(self, agency_name):
        self.__agency_name = agency_name

    def set_jurisdiction(self, jurisdiction):
        self.__jurisdiction = jurisdiction

    def set_contact_information(self, contact_information):
        self.__contact_information = contact_information

