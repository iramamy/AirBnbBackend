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
def properties_list(request):
    properties = models.Property.objects.all()
    serializer = serializers.PropertySerializers(
        properties,
        many=True,
    )

    return Response({"data": serializer.data})
