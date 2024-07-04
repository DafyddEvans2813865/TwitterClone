from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import Profile, Bolt, SharedBolt
from .forms import LoginForm, BoltPostForm, ProfilePicForm, ProfileBioForm


def home(request):
    context_dict = {}
    context_dict['bolts'] = Bolt.objects.all().order_by("-created_at") 

    if request.user.is_authenticated:

        ##check if user is trying to post a bolt 
        form = BoltPostForm(request.POST or None)
        context_dict["form"] = form
        if request.method == "POST":
            if form.is_valid():
                bolt = form.save(commit=False)
                bolt.user = request.user
                bolt.save()
                
    return render(request, 'home.html', context=context_dict)

def about(request):
    return render(request,'about.html', {})

def profile(request, pk):
    if request.user.is_authenticated:
        context_dict = {}

        profile = Profile.objects.get(user=pk)
        bolts = Bolt.objects.filter(user=pk).order_by("-created_at")
        shared_bolts = SharedBolt.objects.filter(user=pk).select_related('bolt')
    
        context_dict['profile'] = profile
        context_dict['bolts'] = bolts
        context_dict['shared_bolts'] = shared_bolts

        #request to follow or unfollow the user  
        if request.method == 'POST':

            if 'follow_user' in request.POST:
                request.user.profile.follows.add(profile)
            
            elif 'unfollow_user' in request.POST:
                request.user.profile.follows.remove(profile)


    return render(request, 'profile.html',context=context_dict)

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
        return redirect('home')  
    return render(request, 'register.html', context_dict)
        
def profile_settings(request):

    context_dict ={}
    context_dict['user'] = request.user
    user_profile = Profile.objects.get(user = request.user)

    Profile_pic_form = ProfilePicForm(request.POST or None,request.FILES or None, instance=user_profile)
    Profile_bio_form = ProfileBioForm(request.POST or None,request.FILES or None, instance=user_profile)

    context_dict['Profile_pic_form'] = Profile_pic_form
    context_dict['Profile_bio_form'] = Profile_bio_form
   
    if Profile_pic_form.is_valid():
        Profile_pic_form.save()
    if Profile_bio_form.is_valid():
        Profile_bio_form.save()

    return render(request,'profile_settings.html',context_dict)

def profile_list(request):
    context_dict = {}
    
    if request.user.is_authenticated:
        #list of all user excluding self 
        context_dict['profiles'] = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html',context_dict)

def bolt_like(request, pk):
    if request.user.is_authenticated:
        bolt = get_object_or_404(Bolt, id=pk)

        #if user already likes bolt remove them 
        if bolt.likes.filter(id=request.user.id):
            bolt.likes.remove(request.user)
        else:
            bolt.likes.add(request.user)
    #'redirects' user to current url 
    return redirect(request.META.get("HTTP_REFERER"))
    
def bolt_share(request, pk):
    if request.user.is_authenticated:
        bolt = get_object_or_404(Bolt, id=pk)

        # Check if this bolt has already been shared by the user
        if SharedBolt.objects.filter(user=request.user, bolt=bolt).exists():
            shared_bolt = SharedBolt.objects.filter(user=request.user, bolt=bolt).first().delete()
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            # Create a new SharedBolt record
            
            SharedBolt.objects.create(user=request.user, bolt=bolt)
            return redirect(request.META.get("HTTP_REFERER"))
        
def search(request):
    context_dict = {}

    query = request.GET.get('search_query', '')
    print("works")

    if query:
        print("user")
        results = Profile.objects.filter(user__username__icontains = query)  
    else:
        print("no user")
        results = Profile.objects.all()  # handle the case when no search query is provided
    
    context_dict['search_query'] = query
    context_dict['profiles'] = results

    return render(request, 'search.html', context_dict)
    
def delete_bolt(request, pk):
    if request.user.is_authenticated:
        bolt = get_object_or_404(Bolt, id=pk)

        ##check that user is the owner of the bolt 
        if request.user.id ==  bolt.user.id:
            bolt.delete()     
            return redirect(request.META.get("HTTP_REFERER")) 
    else:
        messages.success(request, ("Please log In"))
        return redirect(request.META.get("HTTP_REFERER"))
