from django.shortcuts import render
from rest_framework import viewsets
from .models import Exercicio
from .serializers import ExercicioSerializer

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
