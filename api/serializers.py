from rest_framework import serializers
from .models import Todos
from django.contrib.auth.models import User


class TodosSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Todos
        fields = ('id', 'title', 'due_datetime', 'date_created', 'date_modified', 'status', 'owner',)
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todos.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'todos')
