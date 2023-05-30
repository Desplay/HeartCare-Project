import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.patients import ReturnDataPatientsLobby

class WSLobby(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps(ReturnDataPatientsLobby()))
        return
    
    async def disconnect(self, any):
        return
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        if not (data['method'] == 'SyncLobby'):
            return
        await self.send(text_data=json.dumps(ReturnDataPatientsLobby()))
        return