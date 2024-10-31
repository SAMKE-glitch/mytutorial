from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User  # Import User model to access user data

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Display the owner's username
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')  # Link to the highlighted snippet

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)  # Link to each of the user's snippets

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']  # Include user URL, ID, username, and associated snippets

