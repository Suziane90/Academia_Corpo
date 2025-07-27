from django.shortcuts import render
from rest_framework import viewsets
from .models import Treino
from .serializers import TreinoSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer
