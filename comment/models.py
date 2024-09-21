from django.contrib.auth.models import User
from django.db import models

from book.models import BookModel


class CommentModel(models.Model):
    name = models.TextField()
    user = models.ForeignField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
