from django.shortcuts import render
from django.views import View

from django.shortcuts import render
from teachers.models import Teacher

# Create your views here.

class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {'teachers': teachers}
        return render(request,'teacher.html',context)


