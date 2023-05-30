import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.patients import ReturnDataPatientsQueue
from HospitalManager.Models.doctors import dataRender


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
