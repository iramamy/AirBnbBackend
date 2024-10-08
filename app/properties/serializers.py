"""Serializers for the property api view"""

from rest_framework import serializers
from useraccount.serializers import UserDetailSerializer

from . import models


class PropertyListSerializers(serializers.ModelSerializer):
    """Serializer for Property objects"""

    class Meta:
        model = models.Property
        fields = [
            "id",
            "title",
            "price_per_night",
            "image_url",
        ]


class PropertyDetailSerializers(serializers.ModelSerializer):
    """Serializer for property detail objects"""

    landlord = UserDetailSerializer(
        read_only=True,
        many=False,
    )

    class Meta:
        model = models.Property
        fields = [
            "id",
            "title",
            "description",
            "price_per_night",
            "image_url",
            "bedrooms",
            "guests",
            "landlord",
            "country",
            "category",
        ]


class ReservationListSerializer(serializers.ModelSerializer):
    """Serializer for reservation objects"""

    property = PropertyListSerializers(read_only=True, many=False)

    class Meta:
        model = models.Reservation
        fields = (
            "id",
            "start_date",
            "end_date",
            "number_of_nights",
            "total_price",
            "property",
        )
