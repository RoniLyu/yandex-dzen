from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Author, User
from .serializers import AuthorRegisterSerializer
from .permissions import OwnerOrReadOnlyPermission


class AuthorRegisterAPIView(generics.CreateAPIView):
    """
        API для регистрации пользователей
    """
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user.user)
        return Response({'token': token.key})


class AuthorRetrieveUpdateDestroy(viewsets.ModelViewSet):
    """
        API для детального просмотра, изменения и удаления пользователей
    """
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    lookup_field = 'user__username'
    permission_classes = [OwnerOrReadOnlyPermission, ]


