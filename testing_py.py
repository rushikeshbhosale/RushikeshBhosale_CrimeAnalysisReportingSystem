import unittest
from dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.Incident import Incident
from entity.Cases import Case
from entity.IncidentType import IncidentType


class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisServiceImpl()

    def test_create_incident(self):
        incident = Incident(None, "Theft", "2024-05-10", "12.345", "98.765", "Theft occurred", "Open", "1", "4")
        result = self.service.createIncident(incident)
        self.assertTrue(result)
        self.assertIsNotNone(incident.get_incident_id())
        self.assertEqual(incident.get_incident_type(), "Theft")
        self.assertEqual(incident.get_incident_date(), "2024-05-10")
        self.assertEqual(incident.get_location_latitude(), "12.345")
        self.assertEqual(incident.get_location_longitude(), "98.765")
        self.assertEqual(incident.get_description(), "Theft occurred")
        self.assertEqual(incident.get_status(), "Open")
        self.assertEqual(incident.get_victim_id(), "1")
        self.assertEqual(incident.get_suspect_id(), "4")

    def test_update_incident_status(self):
        incident_id = 1
        new_status = "Closed"
        result = self.service.updateIncidentStatus(new_status, incident_id)
        self.assertTrue(result)
        updated_incident = self.service.getIncidentById(incident_id)
        self.assertEqual(updated_incident.get_status(), new_status)

if __name__ == '__main__':
    unittest.main()

