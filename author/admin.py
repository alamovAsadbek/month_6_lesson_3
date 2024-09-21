from django.contrib import admin

from .models import AuthorModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'status', 'created_at', 'updated_at')
    link_display = ('first_name', 'last_name', 'username', 'status', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'username')


admin.site.register(AuthorModel, AuthorAdmin)
