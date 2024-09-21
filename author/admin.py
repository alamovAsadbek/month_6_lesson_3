from django.contrib import admin

from author.models import AuthorModel

admin.site.register(AuthorModel)


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'created_at', 'updated_at')
    link_display = ('first_name', 'last_name', 'username', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'username', 'phone')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
