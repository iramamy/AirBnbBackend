from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from . import models
from . import serializers
from properties.serializers import ReservationListSerializer


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


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request, pk):
    user = models.User.objects.get(pk=pk)
    serializer = serializers.UserDetailSerializer(
        user,
        many=False,
    )

    return Response(serializer.data)


@api_view(["GET"])
def reservation_list(request):
    reservation = request.user.reservations.all().order_by("-created_at")
    serializer = ReservationListSerializer(reservation, many=True)

    return Response(serializer.data)
