from django.contrib import admin

# Register your models here.
from courses.models import Course,Category,Comment
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Comment)