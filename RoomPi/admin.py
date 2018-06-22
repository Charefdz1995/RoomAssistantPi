from django.contrib import admin
from .models import *

admin.site.register(alarm)
admin.site.register(device)
admin.site.register(light)
admin.site.register(fan)
admin.site.register(door)

