# entity/Suspect.py

class Suspect:
    def __init__(self, suspect_id=None, first_name=None, last_name=None, date_of_birth=None, gender=None, address=None,
                 phone_number=None):
        self.__suspect_id = suspect_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__address = address
        self.__phone_number = phone_number

    # Getters
    def get_suspect_id(self):
        return self.__suspect_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    # Setters
    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

