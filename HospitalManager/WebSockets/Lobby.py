import json
from channels.generic.websocket import AsyncWebsocketConsumer
from HospitalManager.Models.patients import ReturnDataPatientsLobby

"""
Class xử lý các request từ client từ Lobby
"""
class WSLobby(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps(ReturnDataPatientsLobby()))
        return
    
    async def disconnect(self, any):
        return
    
    """
    Hàm nhận request từ client và trả về hàng đợi của bác sĩ
    """
    async def receive(self, text_data):
        data = json.loads(text_data)
        if not (data['method'] == 'SyncLobby'):
            return
        await self.send(text_data=json.dumps(ReturnDataPatientsLobby()))
        return