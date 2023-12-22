from django.utils.timezone import now
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'created', 'due_date']

    def validate(self, attrs):
        attrs = super().validate(attrs)

        due_date = attrs['due_date']

        if due_date < now():
            raise serializers.ValidationError({"due_date": "Due date cannot be earlier than the creation date."})

        return attrs
