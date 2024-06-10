from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class Vacancy(models.Model):
    STYLES = (
        ('FL', "To'liq Band"),
        ('PT', "Yarim Band"),
        ('RT', "Masofaviy"),
    )
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=5, choices=STYLES, default='FL')
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateField(default=timezone.now().date() + timedelta(days=10))
    qualification = models.TextField()
    job_duties = models.TextField()
    opportunities = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Person(AbstractUser):

    phone_number = models.CharField(max_length=15, unique=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    is_kadr = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default_manager.jpg')
    works = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

