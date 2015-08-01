# Phonebook-App
A python-django based phonebook app to manage all your contacts.
Django-Phonebook App

Supported Version
Master branch is for Django 1.8+

Installing the app
clone via git and python setup.py install

Setting up the app
Assuming you have Django installed and this app installed (easy_install django-phonebook),
1. python manage.py syncdb
2. Add addressbook.urls to your urls:
url(r'^phonebook/', include('phonebook.urls')),

Setup the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    }
}






