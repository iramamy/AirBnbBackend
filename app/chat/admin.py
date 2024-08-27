"""Chat model customization"""

from django.contrib import admin
from . import models


class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "get_users",
        "created_at",
        "modified_at",
    )

    def get_users(self, obj):
        return ", ".join([user.name for user in obj.users.all()])

    get_users.short_description = "Users"


class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = (
        "conversation",
        "sent_to",
        "created_by",
        "created_at",
    )


admin.site.register(models.Conversation, ConversationAdmin)
admin.site.register(models.ConversationMessage, ConversationMessageAdmin)
