from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.permissions import IsOwner

from .models import Task
from .serializers import TaskSerializer


class ListTask(ListCreateAPIView):
    """
    List all tasks, or create a new task.
    """

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class RetrieveUpdateDestroyTask(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.
    """

    permission_classes = (IsOwner,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
