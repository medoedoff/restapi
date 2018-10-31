from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Library


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ('id', 'author', 'book_title', 'published', 'description', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    library = serializers.PrimaryKeyRelatedField(many=True, queryset=Library.objects.all())

    class Meta:
        model = User
        field = ('id', 'user', 'library')
