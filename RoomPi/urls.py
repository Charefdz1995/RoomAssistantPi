from django.urls import path
from django.contrib.auth import views
from RoomPi.forms import LoginForm
from . import views as view

urlpatterns = [
    path('login/',views.login,{'authentication_form':LoginForm}),
    path('', view.home, name='Home'),
    path('dashboard/', view.dashboard, name='Dashboard'),
    path('devices/', view.devices, name='Devices'),
    path('add', view.addalarm , name='add'),
    path('add2', view.adddevice, name='add2'),
    path('switchon/<light_id>',view.switchOn,name='switchon'),
    path('switchoff/<light_id>',view.switchOff,name='switchoff'),
    path('open/<door_id>',view.open,name='open'),
    path('close/<door_id>', view.close, name='close'),
    path('alarmoff/<alarm_id>', view.alarmoff, name='alarmoff'),
    path('alarmon/<alarm_id>', view.alarmon, name='alarmon'),
    path('delete_light/<light_id>',view.delete_light,name='delete_light'),
    path('delete_door/<door_id>',view.delete_door,name='delete_door'),
    path('delete_fan/<fan_id>',view.delete_fan,name='delete_fan'),
    path('delete_alarm/<alarm_id>',view.delete_alarm,name='delete_Alarm'),
]
