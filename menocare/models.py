from django.db import models
from django.urls import reverse


'''***********************Dentist***************************'''
class Pricing(models.Model):
	service_name = models.CharField(max_length=400, null=True)
	stage = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)

	def __str__(self):
		return self.service_name


class Contact(models.Model):
	client_name = models.CharField(max_length=100, null=True)
	client_email = models.EmailField()
	client_msg = models.TextField()

	def __str__(self):
		return self.client_name


class Appointment(models.Model):
	client_name = models.CharField(max_length=100, null=True)
	client_phone = models.CharField(max_length=100, null=True)
	client_email = models.EmailField()
	client_address = models.CharField(max_length=100, null=True)
	appt_time = models.CharField(max_length=100, null=True)
	appt_day = models.CharField(max_length=100, null=True)
	client_msg = models.TextField()

	def __str__(self):
		return self.client_name


'''***********************Blog***************************'''

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(default="default.jpg", upload_to='images')


	slug = models.SlugField(max_length=200, unique=True)
	author = models.CharField(default="MenoCare", max_length=200, unique=True, null=True)
	
	#status = models.IntegerField(choices=STATUS, default=0)


	def __str__(self):
		return self.title

	
	class Meta:
		ordering = ['-created_on']

	def get_absolute_url(self):
		kwargs = {'slug': self.slug} #, 'pk':self.id}

		return reverse("blog_detail", kwargs=kwargs)

	def save(self, *args, **kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)

	

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(default="default.jpg", upload_to='images')
	active = models.BooleanField(default=True)


	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return 'Comment {self.body} by {self.name}'

	def snippet(self):
		return self.body[:100] + "..."



class Testimonial(models.Model):
	patient_name = models.CharField(max_length=80)
	content = models.TextField()
	who = models.CharField(default="Dental Patient", max_length=80)
	created_on = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(default="default.jpg", upload_to='images')

	def __str__(self):
		return '{self.patient_name}'
