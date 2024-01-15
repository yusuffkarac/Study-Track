from django.contrib import admin
from .models import Products, Days, Activity,Lectures,Grades,Studies,TransferCodes,ProfilePhoto
# Register your models here.

admin.site.register(Products)
admin.site.register(Lectures)
admin.site.register(Days)
admin.site.register(Activity)
admin.site.register(Grades)
admin.site.register(Studies)
admin.site.register(TransferCodes)
admin.site.register(ProfilePhoto)


