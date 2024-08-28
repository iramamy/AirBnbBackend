"""api for chat models"""

from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializers


@api_view(["GET"])
def conversation_list(request):
    serializer = serializers.ConversationListSerializer(
        request.user.conversations.all(), many=True
    )

    return Response(serializer.data)


@api_view(["GET"])
def conversation_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)
    conversation_serializer = serializers.ConversationDetailSerializer(
        conversation,
        many=False,
    )

    message_serializer = serializers.ConversationMessageSerializer(
        conversation.messages.all(),
        many=True,
    )

    return Response(
        {
            "conversation": conversation_serializer.data,
            "messages": message_serializer.data,
        }
    )


@api_view(["GET"])
def conversation_start(request, user_id):
    conversations = models.Conversation.objects.filter(
        users__in=[user_id],
    ).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()

    else:
        user = models.User.objects.get(pk=user_id)
        conversation = models.Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(user)

    return Response(
        {
            "success": True,
            "conversation_id": conversation.id,
        }
    )
