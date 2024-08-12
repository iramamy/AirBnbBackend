"""Property serializers"""

from rest_framework import serializers
from . import models


class PropertySerializers(serializers.ModelSerializer):
    """Serializer for Property objects"""

    class Meta:
        model = models.Property
        fields = [
            "id",
            "title",
            "price_per_night",
            "image_url",
        ]
