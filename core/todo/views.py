from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import TodoTask
from .serializers import (TaskSerializer, TaskCreateSerializer,
                          EditTaskSerializer)
from .permissions import IsOwner


class Tasks(APIView):
    """
        Get list of all tasks
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = TodoTask.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class CreateTask(CreateAPIView):
    """
        Create new task instance
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = TaskCreateSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()
            return Response(
                TaskCreateSerializer(task).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Task(RetrieveUpdateDestroyAPIView):
    """
        Retrive, update or delete a task instance
    """
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = EditTaskSerializer
    queryset = TodoTask.objects.all()
    lookup_field = 'id'

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()
