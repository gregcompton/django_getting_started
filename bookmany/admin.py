from django.contrib import admin

from bookmany.models import Author, Authored, Book

admin.site.register(Author)
admin.site.register(Authored)
admin.site.register(Book)
