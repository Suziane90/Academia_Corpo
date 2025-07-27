from rest_framework import serializers
from .models import Personal
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class PersonalSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Personal
        fields = ['id', 'user', 'descricao']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        personal = Personal.objects.create(user=user, **validated_data)
        return personal
