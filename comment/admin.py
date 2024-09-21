from django.contrib import admin

from comment.models import CommentModel


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_full_name', 'book_id', 'created_at')
    list_display_links = ('id', 'name', 'user_id', 'book_id', 'created_at')
    search_fields = ('name', 'user_id', 'book_id')
