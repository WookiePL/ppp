from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, permissions
from rest_framework import generics
from oauth2_provider.models import Application

from poems.api.serializers import AuthorSerializer, PoemSerializer, ApplicationSerializer, UserProfileSerializer, \
    UserSerializer, CommentSerializer
from poems.models import Author, Poem, Comment


class ApplicationView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Application.objects.filter(name=name)


class AuthorsView(generics.ListAPIView):
    authentication_classes = []
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PoemView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class PoemsView(generics.ListAPIView):
    authentication_classes = []
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


# User profile view
class UserProfileView(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permissions_class = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'


class UserRegistration(generics.CreateAPIView):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentView(generics.ListAPIView):
    authentication_classes = []
    #queryset = Comment.objects.all()
    def get_queryset(self):
        poem_id = self.kwargs['poem_id']
        return Comment.objects.filter(poem_id=poem_id)

    serializer_class = CommentSerializer
