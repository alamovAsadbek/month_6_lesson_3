from django.contrib.auth.models import User
from django.db import models

from book.models import BookModel


class CommentModel(models.Model):
    name = models.TextField()
    user = models.ForeignField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
