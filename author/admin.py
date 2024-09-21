from django.contrib import admin

from author.models import AuthorModel

admin.site.register(AuthorModel)


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    link_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
