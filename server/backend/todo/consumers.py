from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
import json
from datetime import datetime, timedelta
from .models import Todo



class TodoConsumer(WebsocketConsumer):
    
    def connect (self):
        print('connected')
        self.accept()
        # self.channel_layer = get_channel_layer()  
        # self.channel_layer.group_add("todo_notifications", self.channel_name)
        self.group_name = 'todo_notifications'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
    
    def send_message(self, event):
        print('send_message')
        message = event['message']
        self.send(text_data=json.dumps({
            'event': 'Send',
            'message': message
        }))

    def todo_notification(self, event):
        print('notification')
        self.send_message(event)

    

