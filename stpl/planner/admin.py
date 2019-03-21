from django.contrib import admin
from .models import Student, Classes, Schedule

# Register your models here.
admin.site.register(Student)
admin.site.register(Classes)
admin.site.register(Schedule)