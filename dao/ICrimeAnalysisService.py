from abc import ABC, abstractmethod
from typing import List, Collection
from datetime import datetime
from entity.Incident import Incident
from entity.Cases import Case
from entity.Report import Report
from entity.IncidentType import IncidentType


class ICrimeAnalysisService(ABC):
    @abstractmethod
    def createIncident(self, incident: Incident) -> bool:
        pass

    @abstractmethod
    def deleteIncidentById(self, incident_id: int) -> bool:
        pass

    @abstractmethod
    def reset_auto_increment(self, table_name: str):
        pass

    @abstractmethod
    def updateIncidentStatus(self, status: str, incident_id: int) -> bool:
        pass

    @abstractmethod
    def getIncidentsInDateRange(self, start_date: datetime, end_date: datetime) -> Collection[Incident]:
        pass

    @abstractmethod
    def searchIncidents(self, criteria: IncidentType) -> Collection[Incident]:
        pass

    @abstractmethod
    def generateIncidentReport(self, incident: Incident, reporting_officer_id: int, report_date: datetime, status: str) -> Report:
        pass

    @abstractmethod
    def createCase(self, case_description: str, case_status: str) -> Case:
        pass

    @abstractmethod
    def getCaseDetails(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def updateCaseDetails(self, case: Case) -> bool:
        pass

    @abstractmethod
    def getAllCases(self) -> List[Case]:
        pass

    @abstractmethod
    def getIncidentById(self, incident_id: int) -> Incident:
        pass

    @abstractmethod
    def getIncidentReport(self, incident_id: int) -> Report:
        pass

    @abstractmethod
    def updateIncidentReportStatus(self, report_id: int, new_status: str) -> bool:
        pass

    @abstractmethod
    def deleteIncidentReport(self, report_id: int) -> bool:
        pass

    @abstractmethod
    def deleteCase(self, case_id: int) -> bool:
        pass
