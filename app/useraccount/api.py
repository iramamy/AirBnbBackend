from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from . import models
from . import serializers


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def email_list(request):
    email = models.User.objects.all()
    serializer = serializers.SignUpSerializer(
        email,
        many=True,
    )

    return Response({"data": serializer.data})
