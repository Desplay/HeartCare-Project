import json
from HospitalManager.Utils.getPath import dataPath

def DoctorData():
    return json.load(open(dataPath().joinpath('Doctors.json'), encoding="utf8"))

def genderData():
    return json.load(open(dataPath().joinpath('Genders.json'), encoding="utf8"))

def diseaseData():
    return json.load(open(dataPath().joinpath('Kind of diseases.json'), encoding="utf8"))

def LobbyData():
    return json.load(open(dataPath().joinpath('Lobby.json'), encoding="utf8"))

def QueueRoomData():
    return json.load(open(dataPath().joinpath('QueueRoom.json'), encoding="utf8"))

def PatientInDoctorRoomData():
    return json.load(open(dataPath().joinpath('DoctorRooms.json'), encoding="utf8"))