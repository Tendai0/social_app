from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Tweet 
from .forms import TweetForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import forms



def index(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, "Your tweet has been posted")
                return redirect('index')

        tweets = Tweet.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'tweets': tweets, "form": form})
    else:
        tweets = Tweet.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'tweets': tweets})


def profile_list(request):
    if request.user.is_authenticated:
       profiles = Profile.objects.exclude(user=request.user)
       return render(request,'profile_list.html',{"profiles":profiles})
    else:
        messages.success(request,("You must be logged In to view this page"))
        return redirect('index')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id = pk)
        #Post Form Logic
        if request.method == "POST":
            #Get current user 
            current_user_profile = request.user.profile
            #Get Form Data
            action = request.POST['follow']
            #Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow" :
                current_user_profile.follows.add(profile)
            #save profile
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile,"tweets":tweets})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('index')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You have been logged In."))
            return redirect('index')
        else:
            messages.success(request, ("There was an error Loging In"))
            return redirect('login')
    else:   
        return render(request, "login.html", {})

def logout_user(request):
      logout(request)
      messages.success(request, ("You have been logged Out"))
      return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            #Log in User
            user =authenticate(username = username,password=password)
            login(request,user)
            messages.success(request, ("You have been Registerd"))
            return redirect('index')
        
    return render(request, "register.html", {'form':form})
