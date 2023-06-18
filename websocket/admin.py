from django.contrib import admin

from .models import CustomChat


@admin.register(CustomChat)
class CustomChatAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
