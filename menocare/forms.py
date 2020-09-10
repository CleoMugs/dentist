from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['client_name', 'client_email', 'client_msg']