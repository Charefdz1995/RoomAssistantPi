from django.db import models

class device(models.Model):
    name = models.CharField(max_length=45)
    gpio = models.CharField(max_length=2)
    enable = models.CharField(max_length=1,default='0')
    num = models.IntegerField



class alarm(models.Model):
    name = models.CharField(max_length=45)
    gpio = models.CharField(max_length=2)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=20)
    enable = models.BooleanField(default=True)
    buzzer = models.CharField(max_length=2,default="11")



class light(device):
    oncommand = models.CharField(max_length=100)
    offcommand = models.CharField(max_length=100)

class fan(device):
    oncommand = models.CharField(max_length=100)
    offcommand = models.CharField(max_length=100)


class door(device):
    oncommand = models.CharField(max_length=100)
    offcommand = models.CharField(max_length=100)