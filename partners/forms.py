from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'email', 'phone', 'address']
