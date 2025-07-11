from django import forms
from .models import UserProfile
class ContactInformation(forms.Form):
    Phone = forms.IntegerField()
    Address = forms.CharField(max_length=250)
    Place = forms.TimeField()

class mfContactInformation(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['UserName', 'Password', 'Email']
