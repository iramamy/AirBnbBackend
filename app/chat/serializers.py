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
            "modified_at",
        )


class ConversationDetailSerializer(serializers.ModelSerializer):
    """Serializer for Conversation detail object"""

    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Conversation
        fields = (
            "id",
            "users",
            "modified_at",
        )


class ConversationMessageSerializer(serializers.ModelSerializer):
    """Serializer for Conversation message object"""

    sent_to = UserDetailSerializer(many=False, read_only=True)
    created_by = UserDetailSerializer(many=False, read_only=True)

    class Meta:
        model = models.ConversationMessage
        fields = (
            "id",
            "body",
            "sent_to",
            "created_by",
        )
