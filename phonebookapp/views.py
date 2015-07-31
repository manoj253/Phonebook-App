from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from phonebookapp.models import Phonebook
from phonebookapp.forms import PhonebookForm


def contact_list(request):
    contacts = Phonebook.objects.all()
    return render(request, 'phonebookapp/contact_list.html', {'contacts': contacts})

def contact_detail(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    return render(request, 'phonebookapp/contact_detail.html', {'contact': contact})

def create_contact(request):
    if request.method == 'POST':
        form = PhonebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
    else:
        form = PhonebookForm()
    return render(request, 'phonebookapp/create_contact.html', {'form': form})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    if request.method == 'POST':
        form = PhonebookForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-detail', contact_id)
    else:
        form = PhonebookForm(instance=contact)
    return render(request, 'phonebookapp/edit_contact.html', {'form': form})

    
def delete_contact(request, contact_id):
    contact = get_object_or_404(Phonebook, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('/phonebook/')
    return render(request, 'phonebookapp/delete_contact.html', {'contact': contact})