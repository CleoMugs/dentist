from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('pricing.html', views.pricing, name='pricing'),
    path('service.html', views.service, name='service'),
    path('appointment.html', views.appointment, name='appointment'),

    path('blog.html', views.blog, name='blog'),
    path('blog_details.html', views.blog_details, name='blog-details'),


    path('post_to_facebook.html', views.blog_details, name='post_to_facebook'),

]

