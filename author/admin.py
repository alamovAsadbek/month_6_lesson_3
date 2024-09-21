from django.contrib import admin

from .models import AuthorModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'status', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'username')
