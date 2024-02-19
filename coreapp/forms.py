# myapp/forms.py
from django import forms
from .models import user_model

class ChangeApprovalForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.HiddenInput())
    registered = forms.BooleanField(label='Change Registered Status', required=False, widget=forms.HiddenInput())


    class Meta:
        model = user_model
        fields = ['username', 'registered']

class deregisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.HiddenInput())

    class Meta:
        model = user_model
        fields = ['username']