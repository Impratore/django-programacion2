from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Tarea
from .serializers import TareaSerializer, UserSerializer
from rest_framework_simplejwt.authentication import TokenObtainPairView, TokenRefreshView

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated)

class TareaCreateView(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        return Tarea.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TareaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    permission_classes = (permissions.IsAuthenticated)

    def get_queryset(self):
        return Tarea.objects.filter(user=self.request.user)