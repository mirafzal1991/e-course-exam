from django.shortcuts import render
from django.views import View

from django.shortcuts import render,get_object_or_404
from blog.models import Author,Blog
from courses.models import Comment

# Create your views here.

class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {'blogs':blogs}
        return render(request,'blog.html',context)

class BlogDetailView(View):
    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        author = blog.auther_id.all()
        comments = blog.comments.all()

        context = {'blog': blog, 'author': author, 'comments':comments}
        return render(request, 'single.html', context)








