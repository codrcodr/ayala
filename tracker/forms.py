from django import forms
from django.contrib.auth import authenticate
from . import models

class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ('label', 'name')

    def clean(self):
        if self.is_valid():
            label = self.cleaned_data['label']
            name = self.cleaned_data['name']