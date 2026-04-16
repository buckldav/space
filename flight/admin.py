from django.contrib import admin
from .models import FlightControl


# Register your models here.
@admin.register(FlightControl)
class FlightControlAdmin(admin.ModelAdmin):
    pass
