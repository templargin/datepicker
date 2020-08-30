from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateContactREGULAR, CreateContactFormMODAL
from django.views.generic import FormView
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'datepicker/home.html')

class RegularForm(FormView):
    template_name = 'datepicker/regular.html'
    form_class = CreateContactREGULAR
    success_url = '/regular'

def modal(request):
    return render(request, 'datepicker/modal.html')

class ContactCreateView(BSModalCreateView):
    model = Contact
    template_name = "datepicker/create_contact.html"
    form_class = CreateContactFormMODAL
    success_message = 'Success'
    success_url = reverse_lazy('datepicker:index')
