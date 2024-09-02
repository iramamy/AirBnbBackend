"""Serializers for the user api view"""

from rest_framework import serializers
from . import models


class UserListSerializer(serializers.ModelSerializer):
    """Sign up object serializer"""

    class Meta:
        model = models.User
        fields = [
            "email",
            "name",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for user detail objects"""

    class Meta:
        model = models.User
        fields = [
            "id",
            "name",
            "email",
            "avatar_url",
        ]
