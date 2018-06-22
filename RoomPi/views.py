from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , HttpResponse
from .forms import alarmform,deviceform
from django.views.decorators.http import require_POST
from .models import *
from threading import Thread










@login_required(login_url='/login/')
def home(request):
    context = {}
    return render(request,"base.html",context=context)

def dashboard(request):
        Alarmform = alarmform()
        device = deviceform()
        ctxt = {'alarmform': Alarmform,'deviceform':device}
        return render(request,"dashboard.html",context=ctxt)

def devices(request):
    lights_list = light.objects.order_by('id')
    doors_list = door.objects.order_by('id')
    fans_list = fan.objects.order_by('id')
    Alarms_list = alarm.objects.order_by('id')
    context = {'lights_list':lights_list,'doors_list':doors_list,'fans_list':fans_list,'Alarms_list':Alarms_list}
    return render(request,"devices.html",context=context)



@require_POST
def addalarm(request):
    Alarmform = alarmform(request.POST)
    if Alarmform.is_valid():
        print(request.POST['name'])
        Alarm = alarm(name=request.POST['name'],gpio=request.POST['gpio'],email=request.POST['email'],phone=request.POST['phone'],buzzer=request.POST['buzzer'])
        Alarm.save()
    return redirect('Devices')

@require_POST
def adddevice(request):
    devices  = deviceform(request.POST)
    instance = request.POST['type']
    print(instance)
    if devices.is_valid():
        if instance == 'light':
            Light = light(name=request.POST['name'],gpio=request.POST['gpio'],oncommand=request.POST['oncom'],offcommand=request.POST['offcom'])
            Light.save()
        elif instance == 'fan' :
            Fan = fan(name=request.POST['name'],gpio=request.POST['gpio'],oncommand=request.POST['oncom'],offcommand=request.POST['offcom'])
            Fan.save()
        elif instance == 'door':
            Door = door(name=request.POST['name'],gpio=request.POST['gpio'],oncommand=request.POST['oncom'],offcommand=request.POST['offcom'])
            Door.save()
    return redirect('Devices')


def switchOn(request,light_id):
    Light = light.objects.get(pk=light_id)
    output = Light.gpio
    print(output)
    Light.enable = '1'
    Light.save()
    # threadon = lighting(Light.gpio)
    # thread[Light.gpio] = threadon
    # threadon.start()
    return redirect("Devices")


def switchOff(request,light_id):
    Light = light.objects.get(pk=light_id)
    Light.enable = '0'
    Light.save()
    return redirect("Devices")


def open(request,door_id):
    Door = door.objects.get(pk=door_id)
    output = Door.gpio
    Door.enable = '1'
    Door.save()
    return redirect("Devices")


def close(request,door_id):
    Door = door.objects.get(pk=door_id)
    output = Door.gpio
    Door.enable = '0'
    Door.save()
    return redirect("Devices")


def delete_light(request,light_id):
    Light = light.objects.get(pk=light_id)
    Light.delete()
    return redirect("Devices")

def delete_door(request,door_id):
    Door = door.objects.get(pk=door_id)
    Door.delete()
    return redirect("Devices")

def delete_fan(request,fan_id):
    Fan = fan.objects.get(pk=fan_id)
    Fan.delete()
    return redirect("Devices")


def alarmoff(request,alarm_id):
    Alarm = fan.objects.get(pk=alarm_id)
    Alarm.enable = False
    Alarm.save()
    return redirect("Devices")


def alarmon(request,alarm_id):
    Alarm = fan.objects.get(pk=alarm_id)
    Alarm.enable = True
    Alarm.save()
    return redirect("Devices")


def delete_alarm(request,alarm_id):
    Alarm = alarm.objects.get(pk=alarm_id)
    Alarm.delete()
    return redirect("Devices")