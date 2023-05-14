import json
from HospitalManager.Utils.getPath import dataPath

def DoctorData():
    return json.load(open(dataPath().joinpath('Doctors.json'), encoding="utf8"))