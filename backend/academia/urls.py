from os import path
from rest_framework.routers import DefaultRouter
from personal.views import PersonalViewSet
from aluno.views import AlunoViewSt
from users.views import CustomUserViewSet
from django.urls import path, include
from django.contrib import admin
from exercicio.views import ExercicioViewSet
from treino.views import TreinoViewSet

router = DefaultRouter()
router.register(r'usuarios', CustomUserViewSet, basename='customuser')
router.register(r'personal', PersonalViewSet, basename='personal')
router.register(r'alunos', AlunoViewSt, basename='aluno' )
router.register(r'exercicio', ExercicioViewSet)
router.register(r'treino', TreinoViewSet, basename='treino')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('users.urls')),
]
