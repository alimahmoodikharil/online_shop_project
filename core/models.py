from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import CustomUserManager

class CustomUser(AbstractUser):

    username_validator = UnicodeUsernameValidator()
    
    phone_number = models.CharField(verbose_name='Phone Number', max_length=11, unique= True)
    username = models.CharField(max_length=150, unique=True, validators=[username_validator], blank= True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects= CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Otp(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.PROTECT)
    code = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True)




    