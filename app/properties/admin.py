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


class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "property",
        "start_date",
        "end_date",
        "number_of_nights",
        "guests",
        "total_price",
        "created_by",
        "created_at",
    ]

    ordering = ["-created_at"]


admin.site.register(models.Property, PropertyAdmin)
admin.site.register(models.Reservation, ReservationAdmin)
