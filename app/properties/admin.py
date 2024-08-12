"""Property model customization"""

from django.contrib import admin
from . import models


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "price_per_night",
        "bedrooms",
        "guests",
        "landlord",
    ]


admin.site.register(models.Property, PropertyAdmin)
