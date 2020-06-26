import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from Admin.models import Query_table
from django.core import serializers
from .data_analysis import text_mining


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        flag = text_data_json['flag']
        msg = 'not found'
        
        if flag == 0:
            
            find_name = text_mining(message)
            name = find_name.identify_name()

            if(name == '0'):
                name = 'User'
                flag = 2
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type' : 'chat_message',
                    'message': name,
                    'flag' : flag
                }
            )


        p = Query_table
        w = p.objects.filter(quesion__contains = message)
        for i in w:
            msg = i.answer
        
        if flag == 1 :


            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type' : 'chat_message',
                    'message': msg,
                    'flag' : flag
                }
            )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        flag = event['flag']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'flag' : flag
        }))



 
