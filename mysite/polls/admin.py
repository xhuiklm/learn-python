from django.contrib import admin

# Register your models here.
#Dang ky cac bang model de hien thi

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
