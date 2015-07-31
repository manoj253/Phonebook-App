from django.contrib import admin

# Register your models here.
from django.contrib import admin
from phonebookapp.models import Phonebook

admin.site.register(Phonebook)