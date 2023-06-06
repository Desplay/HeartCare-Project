import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.doctors import findDoctor, parseDoctor

"""
Class xử lý các request từ client từ DoctorRoom
"""
class WSDoctorRoom(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        return

    async def disconnect(self, any):
        return
    
    """
    Hàm nhận request từ client và trả về hàng đợi của bác sĩ
    """
    async def receive(self, text_data):
        data = json.loads(text_data)
        if not (data["method"] == "SyncDoctorRoom"):
            return
        await self.send(
            text_data=json.dumps(
                {"Queue": parseDoctor(findDoctor(data["data"]))['Queue']}
            )
        )
        return
