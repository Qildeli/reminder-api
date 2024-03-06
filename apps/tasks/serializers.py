from django.utils.timezone import now
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ("id", "owner", "title", "created", "due_date")
        read_only_fields = ("id", "owner", "created")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = self.context["request"].user.id
        return data

    def validate(self, attrs):
        attrs = super().validate(attrs)

        due_date = attrs["due_date"]

        if due_date < now():
            raise serializers.ValidationError(
                {"due_date": "Due date cannot be earlier than the creation date."}
            )

        return attrs
