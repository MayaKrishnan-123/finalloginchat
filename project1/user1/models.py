from django.db import models
from django.contrib.auth.models import AbstractUser


#model extending the default user  model
class User(AbstractUser):
    address = models.CharField(max_length=80)



