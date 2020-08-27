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


def about(request):
	context = {}
	return render(request, 'about.html', context)


def pricing(request):
	context = {}
	return render(request, 'pricing.html', context)


def service(request):
	context = {}
	return render(request, 'service.html', context)


def appointment(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-scheldule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name +" "+ "Phone: " + your_phone +" "+ '\n' "Email: " + your_email + "Address " +" "+ your_address +"Schedule: " +" "+ your_schedule + '\n' "Day: " + your_date +" "+ " Message: " + your_message

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			['cleobantu@gmail.com'], # to email
			)
	
		context = {'your_name': your_name, 
				   'your_phone': your_phone, 
				   'your_email': your_email,
				   'your_address': your_address,
				   'your_schedule': your_schedule,
				   'your_date': your_date, 
				   'your_message': your_message, 

		}
		return render(request, 'appointment.html', context )

	else:
		#context = {}
		return render(request, 'home.html')