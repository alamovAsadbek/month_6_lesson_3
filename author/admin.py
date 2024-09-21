from django.contrib import admin

from author.models import AuthorModel

admin.site.register(AuthorModel)


class AuthorAdmin(admin.ModelAdmin):
    pass
