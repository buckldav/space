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
        fields = ['completed']
        widgets = {
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'onchange': 'this.form.submit()',
            }),
        }

