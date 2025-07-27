from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from aluno.models import Aluno
from personal.models import Personal


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    tipo = 'desconhecido'

    if hasattr(user, 'aluno'):
        tipo = 'aluno'
    elif hasattr(user, 'personal'):
        tipo = 'personal'

    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'tipo': tipo,
    })
