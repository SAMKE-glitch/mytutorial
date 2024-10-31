from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User  # Import User model to access user data

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Display the owner's username
    highlighted = serializers.ReadOnlyField()  # Include the highlighted code

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlighted']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())  # List of snippet IDs

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']  # Include user ID, username, and associated snippets

