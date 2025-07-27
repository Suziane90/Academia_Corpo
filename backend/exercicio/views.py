from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exercicio
from .serializers import ExercicioSerializer

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(personal=self.request.user.personal)
