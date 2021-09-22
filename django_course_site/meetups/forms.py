from django import forms
from .models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email') #tels django which kind of input field the html has-- it has no relation to any database

    # class Meta:
    #     model = Participant
    #     fields = ['email'] #display only emailfield to the user

