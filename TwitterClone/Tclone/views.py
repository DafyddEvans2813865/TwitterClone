from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Profile, Bolt 
from .forms import LoginForm


def home(request):
    context_dict = {}
    context_dict['bolts'] = Bolt.objects.all().order_by("-created_at") 

    return render(request, 'home.html', context=context_dict)

def about(request):
    return render(request,'about.html', {})

def profile(request, pk):
    if request.user.is_authenticated:
        context_dict = {}

        profile = Profile.objects.get(user=pk)
        context_dict['profile'] = profile
        
        #request to follow or unfollow the user  
        if request.method == 'POST':

            if 'follow_user' in request.POST:
                request.user.profile.follows.add(profile)
            
            elif 'unfollow_user' in request.POST:
                request.user.profile.follows.remove(profile)


    return render(request, 'profile.html',context=context_dict)

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
                return redirect('home')  # Redirect to profile upon successful login
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
        
def profile_list(request):
    context_dict = {}
    
    if request.user.is_authenticated:
        #list of all user excluding self 
        context_dict['profiles'] = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html',context_dict)