from django import forms
from .models import Comment, Contact


class CommentForm(forms.ModelForm):
	name = ''
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')




class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['client_name', 'client_email', 'client_msg']