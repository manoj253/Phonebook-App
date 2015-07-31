from django.db import models

# Create your models here.
import re
from django.db import models
from django.core import validators
from localflavor.us.models import USStateField, PhoneNumberField

class Phonebook(models.Model):  
    first_name = models.CharField(max_length=50, validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid first_name'), 'invalid')
        ])
    last_name = models.CharField(max_length=50, blank=True, validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid last_name'), 'invalid')
        ])
    phone_number = PhoneNumberField(blank=True, help_text=('Put their primary phone number here. '
                                                           'Put additional phone numbers in the Notes field.'))
    email = models.EmailField(blank=True, unique=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True, default="San Francisco", validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z \'\-]+$'), ('Enter a valid city'), 'invalid')
        ])
    state = USStateField(blank=True)
    zip = models.CharField("Zip Code", max_length=5, blank=True,
                           validators=[validators.RegexValidator(re.compile('^\d{5}$'),
                                                                 ('Enter a valid 5 digit zip code'), 'invalid')
        ])
    notes = models.TextField("Notes and Comments", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']