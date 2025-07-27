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
    





    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        # Atualiza campos do aluno
        instance.objetivo = validated_data.get('objetivo', instance.objetivo)
        instance.save()

        #Atualiza campos do usuário aninhado usando o serializer dele
        if user_data:
            user_serializer = CustomUserSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        return instance
