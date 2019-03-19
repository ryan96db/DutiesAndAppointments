import unittest
from DoctorDuties import Duty
from DoctorDuties import AbsenceRequest
import DoctorDuties

class TestDoctorDuties(unittest.TestCase):

    def test_getDay(self):
        d1 = Duty('Mo', 8, 4, 1)
        d2 = Duty('Tu', 9, 5, 2)
        d3 = Duty('We', 10, 3, 3)
        d4 = Duty('Th', 12, 2, 4)
        d5 = Duty('Fr', 13, 4, 5)

        self.assertMultiLineEqual(d1.getDay(), 'Mo')
        self.assertMultiLineEqual(d2.getDay(), 'Tu')
        self.assertMultiLineEqual(d3.getDay(), 'We')
        self.assertMultiLineEqual(d4.getDay(), 'Th')
        self.assertMultiLineEqual(d5.getDay(), 'Fr')

        a1 = AbsenceRequest('Mo', 8, 4, 1)
        a2 = AbsenceRequest('Tu', 9, 5, 2)
        a3 = AbsenceRequest('We', 10, 3, 3)
        a4 = AbsenceRequest('Th', 12, 2, 4)
        a5 = AbsenceRequest('Fr', 13, 4, 5)

        self.assertMultiLineEqual(a1.getDay(), 'Mo')
        self.assertMultiLineEqual(a2.getDay(), 'Tu')
        self.assertMultiLineEqual(a3.getDay(), 'We')
        self.assertMultiLineEqual(a4.getDay(), 'Th')
        self.assertMultiLineEqual(a5.getDay(), 'Fr')

    def test_getHour(self):
        d1 = Duty('Mo', 8, 3, 1)
        a1 = AbsenceRequest('Mo', 9, 4, 2)

        self.assertEqual(d1.getHour(), 8)
        self.assertEqual(a1.getHour(), 9)

    def test_getDuration(self):
        d1 = Duty('Mo', 8, 3, 1)
        a1 = AbsenceRequest('Mo', 9, 4, 2)

        self.assertEqual(d1.getDuration(), 3)
        self.assertEqual(a1.getDuration(), 4)

    def test_getId(self):
        d1 = Duty('Mo', 8, 3, 1)
        a1 = AbsenceRequest('Mo', 9, 4, 2)

        self.assertEqual(d1.getId(), 1)
        self.assertEqual(a1.getId(), 2)

    def test_validAbsenceRequest(self):
        r1 = AbsenceRequest("Mo", 8, 4, 1)
        badRequest = AbsenceRequest("Mo", 16, 12, 1)

        self.assertEqual(DoctorDuties.validAbsenceRequest(r1), 0)
        self.assertEqual(DoctorDuties.validAbsenceRequest(badRequest), 1)

    def test_isInRange(self):
        self.assertTrue(DoctorDuties.isInRange(1, 5, 3), True)
        self.assertFalse(DoctorDuties.isInRange(1, 5, 8), False)

        d2 = Duty("Mo", 9, 5, 2)
        r2 = AbsenceRequest("Mo", 10, 2, 2)

        aBegins = r2.getHour()
        aDur = r2.getDuration()
        aEnds = aBegins + aDur

        dBegins = d2.getHour()
        dDur = d2.getDuration()
        dEnds = dBegins + dDur

        self.assertTrue(DoctorDuties.isInRange(dBegins, dEnds, aBegins), True)
        self.assertTrue(DoctorDuties.isInRange(dBegins, dEnds, aEnds), True)

    def test_conflictingDuties(self):
        duties = []
        requests = []

        d1 = Duty("Mo", 8, 4, 1)
        d2 = Duty("Mo", 9, 5, 2)
        d3 = Duty("Mo", 10, 3, 3)
        d4 = Duty("Mo", 12, 2, 4)
        d5 = Duty("Mo", 13, 4, 5)
        d6 = Duty("Mo", 9, 2, 6)
        d7 = Duty("Mo", 7, 4, 7)
        d8 = Duty("Mo", 15, 1, 8)

        duties.extend([d1, d2, d3, d4, d5, d6, d7, d8])

        r1 = AbsenceRequest("Mo", 1, 7, 1)
        r2 = AbsenceRequest("Mo", 10, 2, 2)
        r3 = AbsenceRequest("Th", 13, 2, 3)

        requests.extend([r1, r2, r3])

        #Only one duty that has a conflicting absence request in this set of lists

        theConflicts = DoctorDuties.conflictingDuties(duties, requests)
        self.assertMultiLineEqual(theConflicts[0].getDay(), "Mo")
        self.assertEqual(theConflicts[0].getHour(), 9)
        self.assertEqual(theConflicts[0].getDuration(), 5)
        self.assertEqual(theConflicts[0].getId(), 2)
      

if __name__ == '__main__':
    unittest.main()



        
        
        
