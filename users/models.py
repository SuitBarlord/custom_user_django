from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class CustomUser(AbstractUser):
    filial = models.CharField(max_length=128, verbose_name='Филиал')
    