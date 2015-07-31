from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'phonebookapp.views.contact_list', name="contact-list"),
    url(r'^(?P<contact_id>\d+)/$',
         'phonebookapp.views.contact_detail', name='contact-detail'),
    url(r'^create/$',
         'phonebookapp.views.create_contact', name="create-contact"),
    url(r'^edit/(?P<contact_id>\d+)/$', 
         'phonebookapp.views.edit_contact', name='edit-contact'),
    url(r'^delete/(?P<contact_id>\d+)/$',
        'phonebookapp.views.delete_contact', name='delete-contact'), 
)        