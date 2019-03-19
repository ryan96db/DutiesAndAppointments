class ApptData:
    def __init__(self, phys_id, appt_id, minutes, event_type):
        self.phys_id = phys_id
        self.appt_id = appt_id
        self.minutes = minutes
        self.event_type = event_type

    def getPhysicianId(self):
        return self.phys_id

    def getAppointmentId(self):
        return self.appt_id

    def getElapsedTime(self):
        return self.minutes

    def getEventType(self):
        return self.event_type

#Class contians a list of data that will contain each part of a patient's visit

class VisitTracker:
    patientVisit = []

    def __init__(self, appointmentId):
        self.appointmentId = appointmentId
        self.isTrackerFinished = False
        
    def addToVisit(self, partOfAppointment):
        self.patientVisit.append(partOfAppointment)

    #returns list of appointment Data objects for each patient
    def getPatientVisit(self):
        self.isTrackerFinished = True
        return self.patientVisit

    def hasTrackerFinished(self):
        return self.isTrackerFinished


def visitIsComplete(theVisit) -> bool:

    #Gets the appointment data that was part of the patient's visit.

    completeVisit = None

    theData = theVisit.getPatientVisit()
    for datum in theData:
        theEvent = datum.getEventType()

        signIn = None
        examRoom = None
        finishVitals = None
        finishPhysician = None

        if(theEvent == "IN"):
            signIn = True

        elif(theEvent == "RM"):
            examRoom = True

        elif(theEvent == "NF"):
            finishVitals = True

        elif(theEvent == "MD"):
            finishPhysician = True

        if ((signIn == True)  and (examRoom == True) and (finishVitals == True)
            and (finishPhysician == True)):
            completeVisit = True
        else:
            completeVisit = False

        return completeVisit

def isDuplicate(a, b) -> bool:
    
    duplicate = None

    aAppt = a.getAppointmentId()
    aEvent = a.getEventType()

    bAppt = b.getAppointmentId()
    bEvent = b.getEventType()

    if ((aAppt == bAppt) and (aEvent == bEvent)):
        duplicate = True
    else:
        duplicate = False

    return duplicate

#Checks physicianId and appointmentId of AppointmentData to see if they are the same

def sameIds(c, d) -> bool:
    same = None

    cPhysId = c.getPhysicianId()
    cAppt = c.getAppointmentId()

    dPhysId = d.getPhysicianId()
    dAppt = d.getAppointmentId()

    if((cPhysId == dPhysId) and (cAppt == dAppt)):
        same = True
    else:
        same = False

    return same

#Searches the unfiltered data for the pieces with the same physId and apptId.

def searchForId(x, physId, apptId):
    dataWithSameIds = []

    for datum in x:
        singularPhysId = datum.getPhysicianId()
        singularApptId = datum.getAppointmentId()

        if ((singularPhysId == physId) and (singularApptId == apptId)):
            dataWithSameIds.append(datum)

    return dataWithSameIds

def removeDanglers(dataWithDanglers, danglingAppointmentId):
    for y in dataWithDanglers:
        if (y.getAppointmentId() == danglingAppointmentId):
            dataWithDanglers.remove(y)

    return dataWithDanglers

#Problem 2, Parts A and B

def cleanData(dirtyData):
    cleanData = []
    indecesWithDuplicates = []
    #Adds first element of dataToClean to a new list since there's nothing to compare that object to.
    #cleanData.append(dirtyData[0])
    #dirtyData.remove(dirtyData[0])

    #Part of function that gets rid of duplicates
    
    for x in range(len(dirtyData)):
        dirty = dirtyData[x]
        for y in range(x + 1):
            if y <= (len(dirtyData)-1):
                clean = dirtyData[y]

            #To remove duplicate stamps from the list
            if (isDuplicate(dirty, clean)):
            #Determines which of the duplicates is most recent
                if (dirty.getElapsedTime() > clean.getElapsedTime()):
                    #cleanData.remove(cleanData[x])
                    #a = cleanData.pop(y)
                    #print(a)
                    #cleanData.append(dirty)
                    #x -= 1
                    #dirtyData.remove(clean)
                    #y += 1

                    #print("When there is a duplicate, X=",x, " and y=", y)
                    indecesWithDuplicates.append(y)
                elif(dirty.getElapsedTime() < clean.getElapsedTime()):
                    #cleanData.append(dirty)
                    #print(y)
                    
                    #The clean value, which is y, had the greater elapsed time
                    indecesWithDuplicates.append(x)
                    
    #print(indecesWithDuplicates)

    dirtyData = [v for i, v in enumerate(dirtyData) if i not in indecesWithDuplicates]
     
    #End of get rid of duplicates


    #Remove Dangling Visits

    for i in range(len(dirtyData)):
        patientVisit = []
        
        for j in range(i + 1, len(dirtyData)):
            clean = dirtyData[i]

            if j <= (len(dirtyData)-1):
                comparer = dirtyData[j]

            #For a piece of data to be considered part of a patient's appointment,
            #the pieces of data in question have to have matching physician Ids
            # and appointment Ids

            if (sameIds(clean, comparer)):
                similarPhysId = clean.getPhysicianId()
                similarAppointmentId = clean.getAppointmentId()

                sameIdData = searchForId(dirtyData, similarPhysId, similarAppointmentId)

                
                patient = VisitTracker(similarAppointmentId)

                if (patient.hasTrackerFinished() == False):
                    for datum in sameIdData:
                        patient.addToVisit(datum)


                #Will remove all ApptData associated with dangling appointmentId

                if (not(visitIsComplete(patient))):
                    dirtyData = removeDanglers(dirtyData, similarAppointmentId)
       
    return dirtyData

#Problem 2, Parts C and D

def waitingAndExamTime(data):
    waitAndExam = []
    global totalUniqueAppointments
    x = 0
    totalUniqueAppointments = 0
    appointmentTracker = 0
    md = 0
    nf = 0
    difference = 0
    waiting = 0
    
    averageWaitTime = 0
    waitingRoomTracker = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            currentData = data[i]
            if j <= (len(data)-1):
                comparer = data[j]
                
            if (sameIds(currentData, comparer)):
                
                similarPhysId = currentData.getPhysicianId()
                similarAppointmentId = currentData.getAppointmentId()

                sameIdData = searchForId(data, similarPhysId, similarAppointmentId)

                
                x = x + 1


            for individualDatum in sameIdData:

                if (individualDatum.getEventType() == "IN"):
                    waiting = individualDatum.getElapsedTime()
                elif (individualDatum.getEventType() == "RM"):
                    exam = individualDatum.getElapsedTime()

                    difference = exam - waiting

                if (difference > 0):
                    waitingRoomTracker += difference

        for dat in sameIdData:
            if (dat.getEventType() == "NF"):
                nf = dat.getElapsedTime()
            elif (dat.getEventType() == "MD"):
                md = dat.getElapsedTime()

            apptExamTime = md - nf

        if (apptExamTime > 0):
            appointmentTracker += apptExamTime

  
    totalUniqueAppointments = x
    averageWaitTime = waitingRoomTracker/totalUniqueAppointments

    averageAppointmentTime = appointmentTracker/totalUniqueAppointments

    waitAndExam.extend([averageWaitTime, averageAppointmentTime])
        
    return waitAndExam



listOfData = []

#Appointments that contain duplicates but are not dangling
a1 = ApptData(1, 3, 5, "IN")
a2 = ApptData(1, 3, 15, "IN")
a3 = ApptData(1, 3, 30, "RM")
a4 = ApptData(1, 3, 45, "NF")
a5 = ApptData(1, 3, 60, "MD")

a6 = ApptData(2, 4, 70, "IN")
a7 = ApptData(2, 4, 75, "IN")
a8 = ApptData(2, 4, 80, "RM")
a9 = ApptData(2, 4, 85, "NF")
a10 = ApptData(2, 4, 90, "MD")

#Dangling Appointment

a12 = ApptData(3, 5, 70, "NF")
a13 = ApptData(3, 5, 75, "MD")

listOfData.extend([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a12, a13])

print("Unfiltered Data: \n")

for datum in listOfData:
    print("Physician ID: ", datum.getPhysicianId(),
          "\tAppointment ID: ", datum.getAppointmentId(),
          "\tMinutes Elapsed Since 8:00 AM: ", datum.getElapsedTime(),
          "\tEvent Type: ", datum.getEventType())

print("Filtered Data: \n")

listOfData = cleanData(listOfData)

for datum in listOfData:
    print("Physician ID: ", datum.getPhysicianId(),
          "\tAppointment ID: ", datum.getAppointmentId(),
          "\tMinutes Elapsed Since 8:00 AM: ", datum.getElapsedTime(),
          "\tEvent Type: ", datum.getEventType(),)

averages = waitingAndExamTime(listOfData)
print("\nAverage Appointment Waiting Time: ", averages[0], " minutes")
print("Average Appointment Exam Time: ", averages[1], " minutes")

print(a12.event_type)

        




    


