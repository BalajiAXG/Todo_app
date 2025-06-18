from django.contrib import admin
from .models import Task

class Adminpanel(admin.ModelAdmin):
    list_display = ("title","completed")

admin.site.register(Task,Adminpanel)
    
