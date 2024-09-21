from django.contrib import admin

from book.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'description', 'created_at', 'updated_at')
    link_display_links = ('name', 'author', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'author', 'description')
