from django.contrib import admin
from django.contrib.auth.models import Group

from comment.models import CommentModel

admin.site.site_header = 'Book Review Admin'

admin.site.unregister(Group)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id', 'book_id', 'created_at')
    list_display_links = ('id', 'name', 'user_id', 'book_id', 'created_at')
    search_fields = ('name', 'user_id', 'book_id')
