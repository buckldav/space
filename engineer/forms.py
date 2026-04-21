from django import forms
from django.db import models
from .models import Task


class TaskViewForm(forms.Form):
    FILTER_CHOICES = [
        ('all', 'All Tasks'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    
    status_filter = forms.ChoiceField(
        choices=FILTER_CHOICES,
        required=False,
        widget=forms.RadioSelect,
        initial='all',
        label='Filter Tasks'
    )
    search = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search tasks by name or description...',
            'class': 'form-control'
        }),
        label='Search'
    )


class TaskListDisplayForm(forms.ModelForm):
   class Meta:
        model = Task
        fields = ['name', 'description', 'completed']
        widgets = {
            'name': forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'readonly': 'readonly',
                'class': 'form-control',
                'rows': 3,
            }),
            'completed': forms.CheckboxInput(attrs={
                'readonly': 'readonly',
                'disabled': 'disabled',
            }),
        }

