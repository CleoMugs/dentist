from django.contrib import admin
from .models import *

# Register your models here.


class PricingAdmin(admin.ModelAdmin):
	list_display = ('service_name', 'stage', 'price')
	list_filter = ("service_name",)
	search_fields = ['service_name']
	

admin.site.register(Pricing, PricingAdmin)
