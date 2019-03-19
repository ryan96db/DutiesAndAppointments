import unittest
from Appointments import ApptData
import Appointments

class TestAppointments(unittest.TestCase):

    def test_getPhysicianId(self):
        a2 = ApptData(1, 3, 15, "IN")
        self.assertEqual(a2.getPhysicianId(), 1)
        
    def test_getAppointmentId(self):
        a2 = ApptData(1, 3, 15, "IN")
        self.assertEqual(a2.getAppointmentId(), 3)
       
    def test_getElapsedTime(self):
        a2 = ApptData(1, 3, 15, "IN")
        self.assertEqual(a2.getElapsedTime(), 15)

    def test_getEventType(self):
        a2 = ApptData(1, 3, 15, "IN")
        a3 = ApptData(1, 3, 30, "RM")
        a4 = ApptData(1, 3, 45, "NF")
        a5 = ApptData(1, 3, 60, "MD")

        self.assertMultiLineEqual(a2.getEventType(), 'IN')
        self.assertMultiLineEqual(a3.getEventType(), 'RM')
        self.assertMultiLineEqual(a4.getEventType(), 'NF')
        self.assertMultiLineEqual(a5.getEventType(), 'MD')

    def test_isDuplicate(self):
        a = ApptData(1, 3, 5, "IN")
        b = ApptData(1, 3, 15, "IN")

        self.assertTrue(Appointments.isDuplicate(a,b), True)

        a7 = ApptData(2, 4, 75, "IN")
        a8 = ApptData(2, 4, 80, "RM")

        self.assertFalse(Appointments.isDuplicate(a7, a8), False)

    def test_sameIds(self):
        a = ApptData(2, 4, 75, "IN")
        b = ApptData(2, 4, 80, "RM")
        
        c = ApptData(1, 3, 15, "IN")

        self.assertTrue(Appointments.sameIds(a,b), True)
        self.assertFalse(Appointments.sameIds(a,c), False)
        

if __name__ == '__main__':
    unittest.main()



        
        
        
