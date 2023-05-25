import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.patients import PatientsLobby

class WSLobby(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps(PatientsLobby.Return()))
        return
    
    async def disconnect(self, any):
        return
    
    async def receive(self, text_data):
        if not (text_data[0] == 'SyncLobby'):
            return
        if(len(json.dumps(text_data[1])) != len(PatientsLobby.Return())):
            await self.send(text_data=json.dumps(PatientsLobby.Return()))
        return