from HospitalManager.Utils.readData import DoctorData
from .Core.queue import Queue
from HospitalManager.Utils.backUp import DoctorRoomBackUp
from HospitalManager.Utils.readData import PatientInDoctorRoomData as Patients

BackUp = []
Doctors = []
"""
Tạo class object Doctor
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
for doctor in DoctorData():
    Node = {
        'Doctor': Doctor(doctor['ID'], doctor['name'], doctor['slot'], doctor['specialist']),
        'Queue': Queue(),
    }
    Doctors.append(Node)
    
for patient in Patients():
    for doctor in Doctors:
        if (patient['DoctorID'] == doctor['Doctor'].ID):
            doctor['Queue'].enqueue(patient['Patient'])
            break
"""
Hàm trả về các bác sĩ
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


"""
Hàm tìm bác sĩ theo ID
"""
def findDoctor(ID):
    for doctor in Doctors:
        if(doctor['Doctor'].ID == ID):
            return doctor
    return None

"""
Hàm trả về các bác sĩ
"""
def parseDoctor(doctor):
    return {
        'Doctor': doctor['Doctor'].__dict__,
        'Queue': doctor['Queue'].Return(),
    }

"""
Hàm xóa bệnh nhân khỏi hàng đợi của bác sĩ
"""
def popPatientFromQueue(doctor):
    for patient in BackUp:
        if (patient['DoctorID'] == doctor['Doctor'].ID):
            BackUp.remove(patient)
            DoctorRoomBackUp(BackUp)
    return doctor['Queue'].dequeue()

"""
Hàm thêm bệnh nhân vào hàng đợi của bác sĩ
"""
def addPatientToQueue(patient):
    for doctor in Doctors:
        if (doctor['Queue'].getLength() < doctor['Doctor'].slot and doctor['Doctor'].specialist == patient['disease']['specialist']):
            doctor['Queue'].enqueue(patient)
            parseData = {
                "DoctorID": doctor['Doctor'].ID,
                "Patient": patient,
            }
            BackUp.append(parseData)
            DoctorRoomBackUp(BackUp)
            return 'Done'
    return 'Fail'