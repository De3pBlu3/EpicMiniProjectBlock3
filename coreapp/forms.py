from django import forms

class changeApprovalForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.HiddenInput())
    registered = forms.BooleanField(label='Change Registered Status', required=False, widget=forms.HiddenInput())


    class Meta:
        fields = ['username', 'registered']

class deregisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.HiddenInput())

    class Meta:
        fields = ['username']

class changeClubForm(forms.Form):
    club_id = forms.IntegerField(label='Club ID', widget=forms.HiddenInput())
    approved = forms.BooleanField(label='Change Approved Status', required=False, widget=forms.HiddenInput())

    class Meta:
        fields = ['club_id', 'approved']

class changeEventAttendanceForm(forms.Form):
    event_id = forms.IntegerField(label='Event ID', widget=forms.HiddenInput())
    username = forms.CharField(label='Username', max_length=255, widget=forms.HiddenInput())
    approved = forms.BooleanField(label='Change Approved Status', required=False, widget=forms.HiddenInput())

    class Meta:
        fields = ['event_id', 'user_id', 'approved']