from rest_framework import viewsets
from .models import Personal
from .serializers import PersonalSerializer

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
