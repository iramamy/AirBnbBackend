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
