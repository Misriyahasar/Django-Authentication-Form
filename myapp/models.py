from django.db import models
from django.forms import ModelForm
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    GENDER_CHOICE=(
        ('M','Male'),
        ('F','Female'),
        ('T','Trans')
    )
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        default='M')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    description = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

  