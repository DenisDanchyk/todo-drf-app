from rest_framework import serializers

from account.models import UserBase
from .models import TodoTask


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    task_is_set_to = serializers.StringRelatedField(many=True)

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
            'title', 'text', 'task_is_set_to', 'image'
        )


class EditTaskSerializer(serializers.ModelSerializer):
    task_is_set_to = serializers.PrimaryKeyRelatedField(
        queryset=UserBase.objects.all(), many=True
    )
    author = serializers.StringRelatedField()

    class Meta:
        model = TodoTask
        fields = (
            'author', 'title', 'text', 'task_is_set_to', 'image',
        )
