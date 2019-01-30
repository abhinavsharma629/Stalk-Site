from django.contrib import admin

# Register your models here.
from .models import StudentData, StudentDetails
admin.site.register(StudentData)
admin.site.register(StudentDetails)