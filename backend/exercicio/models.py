from django.db import models
from django.db import models
from personal.models import Personal


TIPO_GRUPO_MUSCULAR = [
    ('peito', 'Peito'),
    ('costas', 'Costas'),
    ('ombros', 'Ombros'),
    ('biceps', 'Bíceps'),
    ('triceps', 'Tríceps'),
    ('abdomen', 'Abdômen'),
    ('gluteos', 'Glúteos'),
    ('quadriceps', 'Quadríceps'),
    ('posterior_coxa', 'Posterior da Coxa'),
    ('panturrilha', 'Panturrilha'),
    ('antebraco', 'Antebraço'),
]

TIPO_SERIES = [
    (1, '1 série'),
    (2, '2 séries'),
    (3, '3 séries'),
    (4, '4 séries'),
    (5, '5 séries'),
]

TIPO_REPETICOES = [
    (6, '6 reps'),
    (8, '8 reps'),
    (10, '10 reps'),
    (12, '12 reps'),
    (15, '15 reps'),
]

TIPO_DESCANSO = [
    (30, '30 segundos'),
    (45, '45 segundos'),
    (60, '1 minuto'),
    (90, '1 minuto e 30'),
    (120, '2 minutos'),
    (180, '3 minutos ou mais'),
]

TIPO_CARGA = [
    ('leve', 'Leve'),
    ('moderada', 'Moderada'),
    ('padrao', 'Padrão'),
    ('maxima', 'Máxima'),
]

class Exercicio(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='exercicios')
    nome_exercicio = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='media/exercicios/imagens/', blank=True, null=True)
    video = models.FileField(upload_to='media/exercicios/videos/', blank=True, null=True)
    grupo_muscular = models.CharField(max_length=20, choices=TIPO_GRUPO_MUSCULAR, default='peito')
    series = models.PositiveSmallIntegerField(choices=TIPO_SERIES, default=3)
    repeticoes = models.PositiveSmallIntegerField(choices=TIPO_REPETICOES, default=10)
    carga = models.CharField(max_length=10, choices=TIPO_CARGA, default='padrao')
    descanso = models.PositiveSmallIntegerField(choices=TIPO_DESCANSO, default=60)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_exercicio} ({self.grupo_muscular})"


