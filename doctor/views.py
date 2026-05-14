import random

from django.shortcuts import render
from .models import IllCondition
from django import forms

# Create your views here.
def condition_list(request):
	conditions = IllCondition.objects.all()
	malaria = IllCondition.objects.filter(name="Malaria").first()
	malaria_severity = malaria.severity if malaria else 0
		

	conditions = sorted(conditions, key=lambda c: c.severity, reverse=True)
	
	return render(request, "conditions/index.html", {"conditions": conditions, "infected": malaria_severity})#randomNumber is a placeholder, replace with actual value when available


