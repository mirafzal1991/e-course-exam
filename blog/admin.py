from django.contrib import admin

# Register your models here.

from blog.models import Author,Blog
admin.site.register(Author)
admin.site.register(Blog)