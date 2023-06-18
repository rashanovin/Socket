from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json

from .models import CustomChat


class AdminNotify(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):

        try:

            chat = CustomChat.objects.get(question=text_data).answer
        except CustomChat.DoesNotExist:

            chat = 'جوابی برای کلمه ارسال شده وجود ندارد!'

        self.send(text_data=json.dumps({
            'answer': chat,
        }))
