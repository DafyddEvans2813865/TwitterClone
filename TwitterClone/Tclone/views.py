from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request,'about.html', {})

def profile(request):

    context_dict = {}
    context_dict['user'] = request.user

    return render(request,'profile.html', context=context_dict)

def register(request):
    return render(request, "register.html", {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile upon successful login
            else:
                error_message = "Invalid username or password"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user is already made 
        if User.objects.filter(username=username).exists():
            context_dict['error_message'] = "username already exists"
            return render(request, 'register.html', context_dict)
        
        #create user and redirect
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('profile')
    return render(request, 'register.html', context_dict)
        