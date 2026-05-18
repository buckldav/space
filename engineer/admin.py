from django.contrib import admin
from engineer.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass