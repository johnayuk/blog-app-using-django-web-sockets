from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='posts'),
    path('delete/<int:pk>', views.delete_chat, name ='delete'),
]