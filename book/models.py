from django.db import models

from author.models import AuthorModel


class BookModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def book_name(self):
        return self.name

    class Meta:
        verbose_name_plural = "Books"
        verbose_name = "Book"
