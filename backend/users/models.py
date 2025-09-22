from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    foto = models.ImageField(upload_to='media/usuarios/', null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)


