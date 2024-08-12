"""User account customization"""

from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "name",
        "date_joined",
        "is_active",
    ]


admin.site.register(models.User, UserAdmin)
