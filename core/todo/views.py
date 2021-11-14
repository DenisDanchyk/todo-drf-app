from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.mail import send_mail

from .models import TodoTask
from .serializers import (TaskSerializer, TaskCreateSerializer,
                          EditTaskSerializer)
from .permissions import IsOwner


class ListOfTasks(APIView):
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
            serializer.validated_data['author'] = self.request.user
            task = serializer.save()

            if task.task_is_set_to.first() != None:
                send_mail(
                    'New task',
                    f'{task.author} marked you in new task.',
                    'danchyk602@gmail.com',
                    [str(task.task_is_set_to.first())],
                    fail_silently=False,
                )
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleTask(RetrieveUpdateDestroyAPIView):
    """
        Retrive, update or delete a task instance
    """
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = EditTaskSerializer
    queryset = TodoTask.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = self.request.user
            author = serializer.validated_data['author']
            for user in serializer.validated_data['task_is_set_to']:
                send_mail(
                    'New task',
                    f'{author} marked you in new task.',
                    'danchyk602@gmail.com',
                    [str(user)],
                    fail_silently=False,
                )
            return self.update(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()
