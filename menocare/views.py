from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	context = {}
	return render(request, 'home.html', context)


def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['cleophas.mugeni@gmail.com'], # to email
			)

		context = {'message_name':message_name}
		return render(request, 'contact.html', context )

	else:
		#context = {}
		return render(request, 'contact.html')
