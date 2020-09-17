from django.contrib import admin
from .models import *

# Register your models here.


class PricingAdmin(admin.ModelAdmin):
	list_display = ('service_name', 'stage', 'price')

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'client_phone', 'client_email', 
		            'client_address','appt_time', 'appt_day', 
		            'client_msg' )
	
class ContactAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'client_email', 'client_msg')

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'created_on', 'photo')
	prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'body',)
	#prepopulated_fields = {'slug': ('name',)}

admin.site.register(Pricing, PricingAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

