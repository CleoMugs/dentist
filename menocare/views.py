from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

from django.views import generic

from django.http import HttpResponseRedirect

from .forms import CommentForm, ContactForm

from .models import (Pricing, Contact, Appointment, 
					 Post, Comment, Testimonial
					 )

from django.core.paginator import Paginator

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


def comment(request, slug):
	template_name = 'blog_details.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.all()

	new_comment = None

	if request.method == 'POST':

		comment_name = request.POST['message-name']
		comment_email = request.POST['message-email']
		msg = request.POST['message']

		new_comment =  Comment.objects.create(name=comment_name, 
									 		  email=comment_email, 
									 		  body=msg
									 		 )
		new_comment.post = post

		new_comment.save()
		return HttpResponseRedirect(request.path_info)

		context = {'post':post, 'comments':comments, 'new_comment':new_comment }
		return render(request, 'blog_details.html', context )

	else:
		#context = {}
		return render(request, 'blog_details.html')


# function-based views
'''
def blog(request):
	context = {}
	return render(request, 'blog.html', context)
'''


# class-based views
class PostList(generic.ListView):
	template_name = 'blog.html'
	queryset = Post.objects.order_by('-created_on')  # or model = Post
	context_object_name = 'posts' 
	paginate_by = 2
	

def blog_detail(request, slug):
	template_name = 'blog_details.html'
	post = get_object_or_404(Post, slug=slug)

	comments = post.comments.all()

	paginator = Paginator(comments, 2)
	page = request.GET.get('page')
	comments = paginator.get_page(page)
	

	new_comment = None

	if request.method == 'POST':

		comment_form = CommentForm(data=request.POST)

		if comment_form.is_valid():

			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)

			# Assign the current post to the comment
			new_comment.post = post

			# Save the comment to the database
			new_comment.save()
			return HttpResponseRedirect(request.path_info)

	else:
		comment_form = CommentForm()

	context = {'post':post, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
	return render(request, template_name, context)	

	'''
	comment_name = request.POST['message-name']
	comment_email = request.POST['message-email']
	msg = request.POST['message']

	new_comment =  Comment.objects.create(name=comment_name, 
								 email=comment_email, 
								 body=msg)
	new_comment.post.body = post
	print(new_comment)
	new_comment.save()
	#return HttpResponseRedirect(request.path_info)
	context = {'post':post, 'comments':comments, 'new_comment':new_comment }
	return render(request, 'blog_details.html', context )
	'''

def home(request):
	prics = Pricing.objects.all()
	tests = Testimonial.objects.all()
	context = {'prics': prics, 'tests': tests}
	return render(request, 'home.html', context)


def about(request):
	context = {}
	return render(request, 'about.html', context)


def pricing(request):
	prics = Pricing.objects.all()
	context = {'prics': prics}
	return render(request, 'pricing.html', context)


def service(request):
	#####
	template_name = 'service.html'
	posts = Post.objects.order_by('-created_on') 
	paginate_by = 2
	#####

	tests = Testimonial.objects.all()
	context = {'tests': tests, 'posts': posts}

	return render(request, template_name, context)


def post_to_facebook(request):
	context = {}
	return render(request, 'post_to_facebook.html', context)
