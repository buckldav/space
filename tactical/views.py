from django.shortcuts import render
from tactical.models import Phasers
# Create your views here
def tactical(request):
    # get from db
    stuff={"phasers":Phasers.objects.all()}
    
    return render(request, template_name="pages/tactical.html", context=stuff)