from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'surname', 'email', 'number', 'address']
