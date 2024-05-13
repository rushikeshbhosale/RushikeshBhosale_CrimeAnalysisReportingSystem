# entity/IncidentType.py

class IncidentType:
    def __init__(self, type_id=None, type_name=None):
        self.__type_id = type_id
        self.__type_name = type_name

    # Getters
    def get_type_id(self):
        return self.__type_id

    def get_type_name(self):
        return self.__type_name

    # Setters
    def set_type_id(self, type_id):
        self.__type_id = type_id

    def set_type_name(self, type_name):
        self.__type_name = type_name
