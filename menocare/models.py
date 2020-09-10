from django.db import models


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
		return self.service_name


class Appointment(models.Model):
	client_name = models.CharField(max_length=100, null=True)
	client_phone = models.CharField(max_length=100, null=True)
	client_email = models.EmailField()
	client_address = models.CharField(max_length=100, null=True)
	appt_time = models.CharField(max_length=100, null=True)
	appt_day = models.CharField(max_length=100, null=True)
	client_msg = models.TextField()

	def __str__(self):
		return self.service_name