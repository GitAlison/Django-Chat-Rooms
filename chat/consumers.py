import asyncio
import json
from channels.consumer import AsyncConsumer


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print('Conected',dir(event))
        await self.send({
            'type':'websocket.accept'
        })
    async def websocket_receive(self,event):
        text = event.get('text',None)
        dict = json.loads(text)
        msg = dict.get('message')
        print('Message Sended-->',msg)

    async def websocket_disconnect(self,event):
        print('Disconected')