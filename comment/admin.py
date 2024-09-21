from django.contrib import admin

from comment.models import CommentModel

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'post', 'created_at', 'updated_at')
