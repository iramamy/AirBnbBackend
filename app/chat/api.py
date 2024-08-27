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
