from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.contrib.auth.hashers import check_password

from . import models
from . import serializers
from properties.serializers import ReservationListSerializer


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def user_list(request):
    users = models.User.objects.all()
    serializer = serializers.UserListSerializer(
        users,
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


@api_view(["GET"])
def user_detail(request, pk):
    user = models.User.objects.get(pk=pk)
    serializer = serializers.UserDetailSerializer(
        user,
        many=False,
    )

    return Response({"data": serializer.data})


@api_view(["POST", "FILES"])
def edit_user_profile(request):

    if request.method == "POST":

        user_id = request.data.get("user_id")
        email = request.data.get("email")
        name = request.data.get("name")
        avatar = request.FILES.get("avatar_url")

        user, created = models.User.objects.get_or_create(
            id=user_id,
            defaults={
                "email": email,
                "name": name,
                "avatar": avatar,
            },
        )

        if not created:
            user.email = email
            user.name = name
            if avatar:
                user.avatar = avatar
            user.save()

        return Response({"success": True})
    else:
        return Response({"success": False})


@api_view(["POST"])
def change_password(request):
    user = request.user
    user_profile = models.User.objects.get(pk=user.id)

    if request.method == "POST":
        oldPassword = request.data.get("oldPassword")
        password = request.data.get("password")

        if not check_password(oldPassword, user_profile.password):
            return Response({"success": False})

        else:
            user.set_password(password)
            user.save()
            return Response({"success": True})
    return Response({"success": False})
