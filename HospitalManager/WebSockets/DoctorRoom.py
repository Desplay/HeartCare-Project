import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.doctors import findDoctor, parseDoctor


class WSDoctorRoom(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        return

    async def disconnect(self, any):
        return

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
