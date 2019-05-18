from django.contrib import admin
from .models import *


class ModelRegister(admin.ModelAdmin):
    list_display = ['Fullname', 'email', 'phone']


admin.site.register(Register, ModelRegister)
