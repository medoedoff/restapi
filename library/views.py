from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .models import Library
from .serializers import LibrarySerializer, UserSerializer
from .permissions import IsOwnerReadOnly


class BookList(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    throttle_classes = (AnonRateThrottle, UserRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)
    throttle_classes = (AnonRateThrottle, UserRateThrottle,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
