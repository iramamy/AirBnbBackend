"""Serializers for the chat api view"""

from rest_framework import serializers

from . import models
from useraccount.serializers import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    """Serializer for Conversation object"""

    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Conversation
        fields = (
            "id",
            "users",
            "created_at",
        )
