from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=14)
    erp = models.IntegerField(unique=True)
    user_type = models.IntegerField(default=1)
    grade = models.CharField(null=True, max_length=10)
    course = models.CharField(null=True, max_length=32)
    REQUIRED_FIELDS = ['username','email', 'first_name', 'last_name', 'phone', 'grade', 'course']
    USERNAME_FIELD = 'erp'

    def get_username(self):
        return self.erp
    
    def __str__(self):
        return self.username