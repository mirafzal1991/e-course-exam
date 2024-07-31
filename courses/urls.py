from django.urls import path
from courses.views import (IndexView,login_page,register_page,send_email,verify_email_done,
                           verify_email_confirm,logout_page)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('login-page/', login_page, name='login'),
    path('register-page/', register_page, name='register'),
    path('send-mail', send_email, name='send_mail'),
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm'),
    path('logout-page/', logout_page, name='logout'),

]