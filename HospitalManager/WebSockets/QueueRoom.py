import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.patients import ReturnDataPatientsQueue
from HospitalManager.Models.doctors import dataRender

"""
Class xử lý các request từ client từ QueueRoom
"""
class WSQueueRoom(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(
            text_data=json.dumps(
                {"Patients": ReturnDataPatientsQueue(), "Doctors": dataRender()}
            )
        )
        return

    async def disconnect(self, any):
        return

    """
    Hàm nhận request từ client và trả về hàng chờ và chi tiết phòng bác sĩ
    """
    async def receive(self, text_data):
        data = json.loads(text_data)
        if not (data["method"] == "SyncQueueRoom"):
            return
        await self.send(
            text_data=json.dumps(
                {"Patients": ReturnDataPatientsQueue(), "Doctors": dataRender()}
            )
        )
        return
