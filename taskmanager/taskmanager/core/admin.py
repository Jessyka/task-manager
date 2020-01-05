from django.contrib import admin
from taskmanager.tasks.models import Task

# Register your models here.
admin.site.register(Task)