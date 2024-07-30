from django.shortcuts import render
from django.views import View

from courses.models import Category, Course
from teachers.models import Teacher


# Create your views here.

class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()

        contex = {'categories': categories, 'teachers': teachers, 'courses': courses}
        return render(request, 'index.html', contex)
