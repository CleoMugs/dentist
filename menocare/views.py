from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from django.views import generic

from .forms import ContactForm

from .models import Pricing, Contact, Appointment, Post, Comment

# Create your views here.


def contact(request):
	#form = ContactForm()

	if request.method == 'POST':
		#form = ContactForm(request.POST)

		client_name = request.POST['message-name']
		client_email = request.POST['message-email']
		client_msg = request.POST['message']

		obj =  Contact.objects.create(client_name=client_name, 
									 client_email=client_email, 
									 client_msg=client_msg)


		obj.save()

		# send an email
		send_mail(
			client_name, # subject
			client_msg, # message
			client_email, # from email
			['cleophas.mugeni@gmail.com'], # to email
		)

		context = {'client_msg':client_msg}
		return render(request, 'contact.html', context )

	else:
		#context = {}
		return render(request, 'contact.html')


def appointment(request):
	if request.method == 'POST':
		client_name = request.POST['your-name']
		client_phone = request.POST['your-phone']
		client_email = request.POST['your-email']
		client_address = request.POST['your-address']
		appt_time = request.POST['your-scheldule']
		appt_day = request.POST['your-date']
		client_msg = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + client_name +" "+ "Phone: " + client_phone +" "+ '\n' "Email: " + client_email + "Address " +" "+ client_address +"Schedule: " +" "+ appt_time + '\n' "Day: " + appt_day +" "+ " Message: " + client_msg

		obj =  Appointment.objects.create(client_name=client_name, 
									 client_phone=client_phone, 
									 client_email=client_email,
									 client_address=client_address,
									 appt_time=appt_time,
									 appt_day=appt_day,
									 client_msg=client_msg
									 )

		obj.save()

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			client_email, # from email
			['cleophas.mugeni@gmail.com'], # to email
			)
	
		context = {'client_name': client_name, 
				   'client_phone': client_phone, 
				   'client_email': client_email,
				   'client_address': client_address,
				   'appt_time': appt_time,
				   'appt_day': appt_day, 
				   'client_msg': client_msg, 

		}
		return render(request, 'appointment.html', context )

	else:
		#context = {}
		return render(request, 'home.html')


def home(request):
	prics = Pricing.objects.all()
	context = {'prics': prics}
	return render(request, 'home.html', context)


def pricing(request):
	prics = Pricing.objects.all()
	context = {'prics': prics}
	return render(request, 'pricing.html', context)

	
def about(request):
	context = {}
	return render(request, 'about.html', context)


def service(request):
	context = {}
	return render(request, 'service.html', context)



def post_to_facebook(request):
	context = {}
	return render(request, 'post_to_facebook.html', context)



# function-based views
'''
def blog(request):
	context = {}
	return render(request, 'blog.html', context)
'''


# class-based views
class PostList(generic.ListView):
	template_name = 'blog.html'
	queryset = Post.objects.order_by('-created_on') 
	context_object_name = 'posts' 
	paginate_by = 3
	

# class-based views
class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog_details.html'
	query_pk_and_slug = True



def blog_detail(request, slug):
	template_name = 'blog_details.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.all()
	#print('CLEO')

	context = {'post':post, 'comments':comments}
	return render(request, template_name, context)



'''
def blog_detail(request):
	template_name = 'blog_details.html'
	#post = get_object_or_404(Post, pk=pk)
	#comments = post.comments

	context = {}#'post':post, 'comments':comments,}
	return render(request, template_name, context)
'''