from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import status

from .models import TodoTask
from .serializers import TaskSerializer, TaskCreateSerializer


class Tasks(APIView):

    def get(self, request):
        tasks = TodoTask.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class CreateTask(CreateAPIView):

    serializer_class = TaskCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = TaskCreateSerializer(data=request.data)

        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskCreateSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
