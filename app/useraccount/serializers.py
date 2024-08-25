"""User serializers"""

from rest_framework import serializers
from . import models


class SignUpSerializer(serializers.ModelSerializer):
    """Sign up object serializer"""

    class Meta:
        model = models.User
        fields = [
            "email",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer for user detail objects"""

    class Meta:
        model = models.User
        fields = [
            "id",
            "name",
            "avatar_url",
        ]
