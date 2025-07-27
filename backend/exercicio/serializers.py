from rest_framework import serializers
from .models import Exercicio

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome_exercicio', 'grupo_muscular', 'series', 'repeticoes', 'carga']
