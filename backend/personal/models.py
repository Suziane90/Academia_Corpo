from django.db import models
from django.conf import settings


class Personal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.TextField(null = True)

    
    def __str__(self):
        return self.user.get_full_name() or self.user.username