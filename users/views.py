from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializer
from rest_framework import viewsets, permissions
from users.permissions import IsProfileOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsProfileOwnerOrReadOnly)


# class RegistartionsView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
