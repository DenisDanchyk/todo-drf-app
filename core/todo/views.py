from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoTask
from .serializers import TaskSerializer


class Tasks(APIView):
    def get(self, request):
        tasks = TodoTask.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
