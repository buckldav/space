from django.shortcuts import render
from flight.models import FlightControl
from django import forms


# Create your views here.
def flight_view(request):
    # get all Flight objects from DB
    flight_ctrls = FlightControl.objects.all()
    # pass to the template to render
    return render(request, "flight/index.html", {"controls": flight_ctrls})
