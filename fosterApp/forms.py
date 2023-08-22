from django.forms import ModelForm
from .models import *

class ChildForm(ModelForm):
    class Meta:
        model=Child
        fields='__all__'
        exclude=['dateOfBirth']

class SponsorForm(ModelForm):
    class Meta:
        model=Sponsor
        fields='__all__'        