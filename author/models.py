from django.db import models


class AuthorModel(models.Model):
    # Represents the author's first name
    first_name = models.CharField(max_length=50)
    # Represents the author's last name
    last_name = models.CharField(max_length=50)
    # Represents the author's username
    username = models.CharField(max_length=50)
    # Indicates whether the author is active or not
    status = models.BooleanField(default=True)

    # Timestamp of when the author was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp of when the author was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # Returns the author's name when the object is printed
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"
