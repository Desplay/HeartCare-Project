import json
from HospitalManager.Utils.readData import DoctorData
from .Core.Queue import Queue

class Doctor:
    def __init__(self, ID, name, slot, specialist):
        self.ID = ID
        self.name = name
        self.slot = slot
        self.specialist = specialist