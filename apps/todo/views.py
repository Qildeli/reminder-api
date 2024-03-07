from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.permissions import IsOwner

from .models import ToDo
from .serializers import ToDoSerializer


class ListTask(ListCreateAPIView):
    """
    List all todo, or create a new task.
    """

    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(owner=self.request.user)


class RetrieveUpdateDestroyTask(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.
    """

    permission_classes = (IsOwner,)
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
