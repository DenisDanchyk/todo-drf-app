from rest_framework import serializers
from .models import TodoTask


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    task_is_set_to = serializers.StringRelatedField()

    class Meta:
        model = TodoTask
        fields = (
            'id', 'title', 'text', 'author', 'task_is_set_to',
            'created', 'updated', 'image',
        )


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = (
            'title', 'text', 'task_is_set_to', 'image', 'author'
        )


class EditTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = (
            'title', 'text', 'task_is_set_to', 'image'
        )
