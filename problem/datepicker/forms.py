from . models import Contact
from flatpickr import DatePickerInput
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm


class CreateContactFormMODAL(BSModalModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'birthday',
        ]
        widgets = {
             'birthday': DatePickerInput()
        }

class CreateContactREGULAR(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'birthday',
        ]
        widgets = {
             'birthday': DatePickerInput(),
        }
