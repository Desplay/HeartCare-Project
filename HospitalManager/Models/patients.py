import json
from .Core import priorityQueue, queue
from HospitalManager.Utils.getTime import getTime, getDate
from HospitalManager.Utils.generateID import generateID
from HospitalManager.Utils.backUp import LobbyBackUp, QueueBackUp
from HospitalManager.Utils.readData import LobbyData, QueueRoomData


PatientsLobby = priorityQueue.Queue()
PatientsInQueue = queue.Queue()

def RunBackUp():
    for patient in LobbyData():
        PatientsLobby.enqueue(patient)

    for patient in QueueRoomData():
        PatientsInQueue.enqueue(patient)
RunBackUp()

"""
Hàm tạo bệnh nhân mới
"""

def CreatePatient(inputData):
    inputData.update({"PhyID": (str("BN") + str(PatientsLobby.length() + 1))})
    inputData.update({"IDCode": str(generateID())})
    inputData.update({"date": str(getTime())})
    inputData.update({"datetime": int(getDate())})
    inputData['gender'] = json.loads(inputData['gender'].replace("'", '"'))
    inputData['disease'] = json.loads(inputData['disease'].replace("'", '"'))
    PatientsLobby.enqueue(inputData)
    LobbyBackUp(PatientsLobby.Return())
    return

"""
Hàm tìm bệnh nhân theo IDCode
"""
def findPatient(IDCode):
    return PatientsLobby.find(IDCode)

"""
Hàm chỉnh sửa bệnh nhân theo IDCode
"""
def editPatient(inputData):
    PatientsLobby.remove(inputData["IDCode"])
    return CreatePatient(inputData)

"""
Hàm đẩy bệnh nhân vào hàng đợi của phòng chờ
"""
def popPatientLobby():
    patientReady = PatientsLobby.dequeue()
    PatientsInQueue.enqueue(patientReady)
    LobbyBackUp(PatientsLobby.Return())
    QueueBackUp(PatientsInQueue.Return())
    return

"""
Hàm xóa bệnh nhân theo IDCode
"""
def removePatientWithID(IDCode):
    return PatientsLobby.remove(IDCode)

"""
Hàm trả về hàng đợi của phòng tiếp tân
"""
def ReturnDataPatientsLobby():
    return PatientsLobby.Return()


"""
Hàm trả về hàng đợi của phòng chờ
"""
def ReturnDataPatientsQueue():
    return PatientsInQueue.Return()
