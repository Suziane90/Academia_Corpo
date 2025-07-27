from rest_framework import serializers
from .models import Aluno
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class AlunoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Aluno
        fields = ['id', 'user', 'objetivo']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        aluno = Aluno.objects.create(user=user, **validated_data)
        return aluno
