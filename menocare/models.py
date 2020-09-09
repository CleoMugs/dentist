from django.db import models


class Pricing(models.Model):
	service_name = models.CharField(max_length=400, null=True)
	stage = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)

	def __str__(self):
		return self.service_name