from django.contrib import admin
from .models import student_details

# Register your models here.
# admin.site.register(student_details)


@admin.register(student_details)
class student_detailsAdmin(admin.ModelAdmin):
    list_display=['id','name','emailId','age','course']

