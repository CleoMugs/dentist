from django.shortcuts import render

# Create your views here.

def home(request):
	context = {}
	return render(request, 'home.html', context)


def contact(request):
	context = {}
	return render(request, 'contact.html', context)
