from django import forms
from phonebookapp.models import Phonebook

class PhonebookForm(forms.ModelForm):

    first_name = forms.CharField(min_length=3, max_length=50)
    last_name = forms.CharField(min_length=3, max_length=50, required=False)

    class Meta:
        model = Phonebook 