# entity/Officer.py

class Officer:
    def __init__(self, officer_id=None, first_name=None, last_name=None, badge_number=None, rank=None,
                 contact_information=None, agency_id=None):
        self.__officer_id = officer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__badge_number = badge_number
        self.__rank = rank
        self.__contact_information = contact_information
        self.__agency_id = agency_id

    # Getters
    def get_officer_id(self):
        return self.__officer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_badge_number(self):
        return self.__badge_number

    def get_rank(self):
        return self.__rank

    def get_contact_information(self):
        return self.__contact_information

    def get_agency_id(self):
        return self.__agency_id

    # Setters
    def set_officer_id(self, officer_id):
        self.__officer_id = officer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_badge_number(self, badge_number):
        self.__badge_number = badge_number

    def set_rank(self, rank):
        self.__rank = rank

    def set_contact_information(self, contact_information):
        self.__contact_information = contact_information

    def set_agency_id(self, agency_id):
        self.__agency_id = agency_id
