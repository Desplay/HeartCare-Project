from HospitalManager.Utils.readData import DoctorData
from .Core.queue import Queue


"""
Tạo class Doctor
"""
class Doctor:
    def __init__(self, ID, name, slot, specialist):
        self.ID = str(ID)
        self.name = name
        self.slot = slot
        self.specialist = specialist


"""
Tạo mảng chứa các bác sĩ và hàng đợi của bác sĩ
"""
Doctors = []
for doctor in DoctorData():
    Node = {
        'Doctor': Doctor(doctor['ID'], doctor['name'], doctor['slot'], doctor['specialist']),
        'Queue': Queue(),
    }
    Doctors.append(Node)

"""
Tạo hàm trả về các bác sĩ
"""
def dataRender():
    Data = []
    for doctor in Doctors:
        Node = {
            'Doctor': doctor['Doctor'].__dict__,
            'Queue': doctor['Queue'].Return(),
        }
        Data.append(Node)
    return Data

def findDoctor(ID):
    for doctor in Doctors:
        if(doctor['Doctor'].ID == ID):
            return doctor
    return None

def parseDoctor(doctor):
    return {
        'Doctor': doctor['Doctor'].__dict__,
        'Queue': doctor['Queue'].Return(),
    }

def popPatientFromQueue(doctor):
    return doctor['Queue'].dequeue()
"""
Tạo hàm thêm bệnh nhân vào hàng đợi của bác sĩ
"""
def addPatientToQueue(patient):
    for doctor in Doctors:
        if (doctor['Queue'].getLength() < doctor['Doctor'].slot and doctor['Doctor'].specialist == patient['disease']['specialist']):
            doctor['Queue'].enqueue(patient)
            return 'Done'
    return 'Fail'