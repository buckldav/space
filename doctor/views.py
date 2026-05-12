import random

from django.shortcuts import render
from .models import IllCondition
from django import forms

# Create your views here.
def condition_list(request):
	conditions = IllCondition.objects.all()
	conditions = sorted(conditions, key=lambda c: c.severity, reverse=True)
	
	return render(request, "conditions/index.html", {"conditions": conditions, "infected": (random.randint(0, 100)*random.randint(0, 100)/100)})#randomNumber is a placeholder, replace with actual value when available


