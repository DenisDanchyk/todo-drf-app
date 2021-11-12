from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TodoTask

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    task_is_set_to = serializers.StringRelatedField(many=True)

    class Meta:
        model = TodoTask
        fields = (
            'title', 'text', 'author', 'task_is_set_to',
            'created', 'updated', 'image',
        )


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = (
            'title', 'text', 'task_is_set_to', 'image', 'author'
        )