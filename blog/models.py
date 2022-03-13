from pydoc_data.topics import topics
from turtle import title
from django.db import models

# Create your models here.

class Message(models.Model):
    content = models.TextField(max_length=1050)
    topic = models.TextField(max_length=1050)

    timestamp = models.DateTimeField(auto_now_add=True)

    # def __init__(self):
    #     return self.content

    def last_5_messages(self):
        return Message.objects.order_by('-timestamp').all()[:5]