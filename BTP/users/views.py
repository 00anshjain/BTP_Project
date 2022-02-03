from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
from doctors.models import Profile


# from django.conf import settings
# User = settings.AUTH_USER_MODEL


# Create your views here.
def main(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            name = request.POST['first_name'] + ' ' + request.POST['last_name']
            email = request.POST['email']
            age = request.POST['age']
            gender = request.POST['gender']
            username = request.POST['username']
            user = form.save()

            Profile.objects.create(name=name, email=email,
                                   age=age, gender=gender, username=username, user=user)
            pk = Profile.objects.get(username=username).Did
            print(pk)
            msg = 'user created'
            return redirect('doctorRegister', pk)
        else:
            msg = 'form is not valid'
    else:
        form = CustomUserCreationForm()
    return render(request, 'login_register.html', {'form': form, 'msg': msg})


def bookAppointment(request):
    return render(request, 'bookAppointment.html')


def about(request):
    return render(request, 'about.html')


def blogs(request):
    return render(request, 'blogs.html')


def contact(request):
    return render(request, 'contact.html')


def doctors(request):
    return render(request, 'doctors.html')


def review(request):
    return render(request, 'review.html')


def services(request):
    return render(request, 'services.html')


def doctorLogin(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("allDoctors")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("allDoctors")
        else:
            messages.error(request, "Username OR Password is incorrect")
    return render(request, 'doctorLogin.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "user was logged out!")
    return redirect("doctorLogin")
