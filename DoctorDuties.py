class Duty:
    def __init__(self, day, hour, duration, physician_id):
        self.day = day
        self.hour = hour
        self.duration = duration
        self.physician_id = physician_id

    def getDay(self):
        return self.day

    def getHour(self):
        return self.hour

    def getDuration(self):
        return self.duration

    def getId(self):
        return self.physician_id


class AbsenceRequest(Duty):
    pass

def validAbsenceRequest(request) -> int:
    if ((request.getHour() + request.getDuration()) > 23):
        return 1
    else:
        return 0

def isInRange(low, high, numberInQuestion) -> bool:
    if (numberInQuestion > low and numberInQuestion < high):
        return True
    else:
        return False

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

x = validAbsenceRequest(r1)
badRequest = AbsenceRequest("Mo", 16, 12, 1)
y = validAbsenceRequest(badRequest)

print('Successful Absence Request: ', x)
print('Bad Absence Request: ', y)


def conflictingDuties(doctorDuties, absenceRequests):
    conflicts = []
    for duty in doctorDuties:
        dutyId = duty.getId()
        dutyWeekDay = duty.getDay()

        for request in absenceRequests:
            requestId = request.getId()
            requestWeekDay = request.getDay()

            potentialDutyConflict = ((dutyId == requestId) and (dutyWeekDay == requestWeekDay))

            if (potentialDutyConflict == True):
                dutyBegins = duty.getHour()
                dutyDuration = duty.getDuration()
                dutyEnds = dutyBegins + dutyDuration

                absenceBegins = request.getHour()
                absenceDuration = request.getDuration()
                absenceEnds = absenceBegins + absenceDuration

                absenceBeginsInRange = isInRange(dutyBegins, dutyEnds, absenceBegins)
                absenceEndsInRange = isInRange(dutyBegins, dutyEnds, absenceEnds)

                if (absenceBeginsInRange == True or absenceEndsInRange == True):
                    conflicts.append(duty)


    return conflicts


theConflicts = conflictingDuties(duties, requests)

print('\nThe following duties have conflicting absence requests: \n')

for conflict in theConflicts:
    print('Day: ',conflict.getDay(), '\nHour: ', conflict.getHour(),
          '\nDuration: ',conflict.getDuration(), '\nPhysicianID: ', conflict.getId(), '\n')


    
                    









    
