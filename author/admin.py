from django.contrib import admin

from .models import AuthorModel

admin.site.register(AuthorModel)


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'created_at', 'updated_at')
    link_display = ('first_name', 'last_name', 'username', 'created_at', 'updated_at')
