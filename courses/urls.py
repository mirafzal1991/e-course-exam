from django.urls import path
from courses.views import IndexView

urlpatterns = [

    path('home/', IndexView.as_view(), name='index')

]