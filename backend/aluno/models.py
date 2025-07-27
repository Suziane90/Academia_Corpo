from django.conf import settings
from django.db import models
from personal.models import Personal


class Aluno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aluno')
    objetivo = models.CharField(max_length=100)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.nome_completo
