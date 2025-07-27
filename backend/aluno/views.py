from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSt(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
