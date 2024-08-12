"""Property database model"""

import uuid
from django.db import models
from django.conf import settings
from useraccount.models import User


class Property(models.Model):
    """Manager for property"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.IntegerField()
    bedrooms = models.IntegerField()
    guests = models.IntegerField()
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/properties")
    landlord = models.ForeignKey(
        User, related_name="properties", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def image_url(self):
        """Return property image url"""

        return f"{settings.WEBSITE_URL}{self.image.url}"

    def __str__(self):
        return f"{self.title} - {self.landlord}"
