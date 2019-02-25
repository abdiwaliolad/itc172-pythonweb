from django import forms
from .models  import Meeting,Resource

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'
class resourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'