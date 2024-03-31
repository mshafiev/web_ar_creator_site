# forms.py
from django import forms
from .models import ModelStats


class EditModelForm(forms.ModelForm):
    class Meta:
        model = ModelStats
        fields = ['project_name', 'description']

        projectname = forms.CharField(widget=forms.HiddenInput())