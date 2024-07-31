from django.shortcuts import render,redirect
from django.views import View

from courses.models import Category, Course, User
from teachers.models import Teacher
from blog.models import Blog
from django.contrib.auth import authenticate, login, logout
from courses.tokens import account_activation_token
from courses.forms import LoginForm,RegisterModelForm,EmailForm
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages



# Create your views here.

class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        blog = Blog.objects.all()

        contex = {'categories': categories, 'teachers': teachers, 'courses': courses,'blog': blog}
        return render(request, 'index.html', contex)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            if not user.is_active:
                current_site = get_current_site(request)
                user = request.user
                email = request.user.email
                subject = "Verify Email"
                message = render_to_string('verify_email_message.html', {
                    'request': request,
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                email = EmailMessage(
                    subject, message, to=[email]
                )
                email.content_subtype = 'html'
                email.send()
                return redirect('verify-email-done')
            else:
                return redirect('register')
        return render(request, 'verify_email_message.html')
        user.save()

        send_mail('Register','Successfully registered','mirobitovmirafzalpython@gmail.com',[user.email],fail_silently=False)
        return redirect('index')
    else:
        form = RegisterModelForm()
    return render(request, 'register.html',{'form':form})

def send_email(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'],form.cleaned_data['message'],form.cleaned_data['email_from'],[form.cleaned_data['email_to']],fail_silently=False)

            return redirect('index')
    context = {'form': form}
    return render(request,'send-mail.html',context)

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print('-------------------------------')
        print(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email has been verified.')
        return redirect('index')
    else:
        messages.warning(request, 'The link is invalid.')

    return render(request, 'verify_email_confirm.html')


def verify_email_done(request):
    return render(request, 'verify_email_done.html')

def logout_page(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')
