"""Chat database model"""

import uuid
from django.db import models

from useraccount.models import User


class Conversation(models.Model):
    """Manager for chat"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    users = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"


class ConversationMessage(models.Model):
    """Manager for conversation message"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    conversation = models.ForeignKey(
        Conversation,
        related_name="messages",
        on_delete=models.CASCADE,
    )

    body = models.TextField()
    sent_to = models.ForeignKey(
        User,
        related_name="received_messages",
        on_delete=models.CASCADE,
    )

    created_by = models.ForeignKey(
        User,
        related_name="sent_messages",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by.name} - to - {self.sent_to.name}"
