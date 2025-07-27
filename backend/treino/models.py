from django.db import models
from aluno.models import Aluno 
from django.db import models
from personal.models import Personal
from exercicio.models import Exercicio

DIAS_DA_SEMANA = [
    ('segunda', 'Segunda-feira'),
    ('terca', 'Terça-feira'),
    ('quarta', 'Quarta-feira'),
    ('quinta', 'Quinta-feira'),
    ('sexta', 'Sexta-feira'),
    ('sabado', 'Sábado'),
    ('domingo', 'Domingo'),
]

class Treino(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='treinos')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='treinos', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    dia_da_semana = models.CharField(max_length=10, choices=DIAS_DA_SEMANA)
    exercicios = models.ManyToManyField(Exercicio, related_name='treinos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.aluno.user.username} ({self.get_dia_da_semana_display()})"
