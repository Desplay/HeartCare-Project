import json
from .Core import priorityQueue, queue
from HospitalManager.Utils.getTime import getTime, getDate
from HospitalManager.Utils.generateID import generateID


PatientsLobby = priorityQueue.Queue()
PatientsTreatment = queue.Queue()

def CreatePatient(inputData):
    inputData.update({"IDCode": str(generateID())})
    inputData.update({"date": str(getTime())})
    inputData.update({"datetime": int(getDate())})
    inputData['gender'] = json.loads(inputData['gender'].replace("'", '"'))
    inputData['disease'] = json.loads(inputData['disease'].replace("'", '"'))
    PatientsLobby.enqueue(inputData)
    return


def findPatient(IDCode):
    return PatientsLobby.find(IDCode)


def editPatient(inputData):
    PatientsLobby.remove(inputData["IDCode"])
    return CreatePatient(inputData)


def popPatientLobby():
    return PatientsTreatment.enqueue(PatientsLobby.dequeue())

def removePatientWithID(IDCode):
    PatientsLobby.remove(IDCode)
    return


def ReturnDataPatientsLobby():
    return PatientsLobby.Return()


def ReturnDataPatientsQueue():
    return PatientsTreatment.Return()
