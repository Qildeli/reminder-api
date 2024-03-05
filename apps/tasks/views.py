from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.permissions import IsOwner

from .models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    """
    List all tasks, or create a new task.
    """

    permission_classes = (IsOwner,)
    serializer_class = TaskSerializer

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

    permission_classes = (IsOwner,)
    serializer_class = TaskSerializer

    def get_object(self, request, pk):
        try:
            return Task.objects.get(pk=pk, owner=request.self.user)
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
