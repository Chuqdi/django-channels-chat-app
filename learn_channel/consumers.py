import json
from unittest import async_case
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.username = self.scope["url_route"]["kwargs"]["username"]
        self.chat_room = f'chat_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(self.chat_room,self.channel_name)
        async_to_sync(self.accept())
        async_to_sync(self.channel_layer.group_send)(self.chat_room,{'type':'subscription_to_room_successfully'})

    

        

    

    
    def subscription_to_room_successfully(self,e):
        async_to_sync(self.send(text_data=json.dumps({"message":f"Subsription to room {self.room_name} succesful"})))
    
    def receive(self, text_data=None, bytes_code =None):
        data = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(self.chat_room, {
             'type':'message_sent',
             'data':data
        })
        



    def message_sent(self,data):
        username = data['data']['username']
        message = data['data']['message']

        async_to_sync(self.send(text_data =json.dumps({
            "message":message,
            "username":username
        })))



    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)


    
        