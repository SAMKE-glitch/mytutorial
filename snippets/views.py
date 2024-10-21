from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer  # Import SnippetSerializer and UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User  # Import the User model
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly  # Import your custom permission

# Snippet views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # Add permission
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Add permission including your custom permission
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# User views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

