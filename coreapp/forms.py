# myapp/forms.py
from django import forms
from .models import user_model

class userAlterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255)
    registered = forms.BooleanField(label='Change Registered Status', required=False)

    class Meta:
        model = user_model
        fields = ['username', 'registered']


