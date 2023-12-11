from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image')
    date_of_registration = models.DateField(auto_now_add=True, verbose_name='дата регистрации')


    def __str__(self):
        return self.username
