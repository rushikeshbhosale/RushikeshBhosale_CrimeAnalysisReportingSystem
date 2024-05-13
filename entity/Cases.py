# entity/Cases.py

class Case:
    def __init__(self, case_id=None, case_description=None, case_status=None):
        self.__case_id = case_id
        self.__case_description = case_description
        self.__case_status = case_status

    # Getters
    def get_case_id(self):
        return self.__case_id

    def get_case_description(self):
        return self.__case_description

    def get_case_status(self):
        return self.__case_status

    # Setters
    def set_case_id(self, case_id):
        self.__case_id = case_id

    def set_case_description(self, case_description):
        self.__case_description = case_description

    def set_case_status(self, case_status):
        self.__case_status = case_status
