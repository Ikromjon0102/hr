from django.contrib import admin

# Register your models here.
from .models import Vacancy, Person

admin.site.register(Vacancy)
admin.site.register(Person)