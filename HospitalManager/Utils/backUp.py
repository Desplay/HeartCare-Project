import json
from HospitalManager.Utils.getPath import dataPath

def DoctorRoomBackUp(inputData):
    save = open(dataPath().joinpath('DoctorRooms.json'), 'w', encoding="utf8")
    save.write(json.dumps(inputData))
    save.close()
    return

def LobbyBackUp(inputData):
    save = open(dataPath().joinpath('Lobby.json'), 'w', encoding="utf8")
    save.write(json.dumps(inputData))
    save.close()

def QueueBackUp(inputData):
    save = open(dataPath().joinpath('QueueRoom.json'), 'w', encoding="utf8")
    save.write(json.dumps(inputData))
    save.close()