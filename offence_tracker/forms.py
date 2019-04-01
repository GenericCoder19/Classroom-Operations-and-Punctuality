from django import forms
from django.contrib.auth.models import User

from .models import Offence

class OffenceForm(forms.ModelForm):

    class Meta:
        model = Offence
        fields = ['type','block','floor','period','grade','section']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name','last_name']