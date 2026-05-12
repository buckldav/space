from django import forms
from .models import Phasers


class PhaserDirectionForm(forms.ModelForm):
    class Meta:
        model = Phasers
        fields = ["direction_fireing"]
        widgets = {
            "direction_fireing": forms.Select(attrs={"class": "form-select form-select-sm"})
        }
