from rest_framework import serializers
from .models import Treino
from exercicio.serializers import ExercicioSerializer
from exercicio.models import Exercicio

class TreinoSerializer(serializers.ModelSerializer):
    exercicios = ExercicioSerializer(many=True, read_only=True)  # Para exibir nomes e detalhes
    exercicios_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Exercicio.objects.all(),
        write_only=True,
        source='exercicios'
    )

    class Meta:
        model = Treino
        fields = ['id', 'personal', 'titulo', 'descricao', 'dia_da_semana', 'exercicios', 'exercicios_ids', 'criado_em']
