# from django.utils import timezone
from datetime import datetime as dt
import json
from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Message



class blogConsumer(AsyncWebsocketConsumer):


    # @database_sync_to_async
    # def get_message(request):
    #     posts = Message.objects.all()
    #     # Message.objects.order_by('-timestamp').all()[:5]
    #     # return render(request, 'blog/post.html',{'posts':posts})
    #     return posts


    @database_sync_to_async
    def create_post(self, content):
        new_msg = Message.objects.create( content=content)
        new_msg.save()
        return new_msg


    # @database_sync_to_async
    # def delete_chat(self, pk):
    #     delete_msg = Message.objects.get( content=pk)
    #     delete_msg.delete()
    #     return delete_msg



    async def connect(self):
        self.room_group_name = 'blog'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()



    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        timestamp=dt.now()
    
        new_msg = await self.create_post(message)
       

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'blog_post',
                'message':new_msg.content,
                'timestamp':timestamp.isoformat(),
                # 'id':self.id
            }
        )

    async def blog_post(self, event):
        message = event['message']
        timestamp = event['timestamp']
        # id = event['id']


        await self.send(text_data=json.dumps({
            'type':'blog',
            'message':message,
            'timestamp':timestamp,
            # 'id':id
        }))