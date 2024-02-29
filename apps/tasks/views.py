from django.http import Http404
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    """
    List all tasks, or create a new task.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetail(APIView):
    """
    Retrieve, update or delete a task instance.
    """
    serializer_class = TaskSerializer

    @staticmethod
    def get_object(request, pk):
        try:
            return Task.objects.get(pk=pk, owner=request.user)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
