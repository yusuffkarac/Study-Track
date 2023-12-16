from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_request(request):
    if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')


    return render(request, 'account/login.html')

def register_request(request):
    if request.method == 'POST':
        name = request.POST["name"]
        surname = request.POST["surname"]
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            return render(request, 'account/register.html',{
                
                'error':'Bu kullanıcı adı zaten alınmış.',
                'name' : name,
                'surname' : surname,

                })
        else:

            user = User.objects.create_user(username=username, password=password,first_name=name,last_name=surname)
            user.save()
        return redirect('login')
    return render(request, 'account/register.html')

def logout_request(request):
    logout(request)
    return redirect('login')
