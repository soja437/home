from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

# Create your views here.

def login(request):

    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def about(request):
    if request.user.is_authenticated:


        return render(request,'about.html')
    else:
        return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def usercreate(request):
    if request.method=='POST':
       
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       password=request.POST['password1']
       cpassword=request.POST['password2']
       email=request.POST['email']

       if password==cpassword:
           if User.objects.filter(username=username):
              messages.info(request,'This username already exists!!!!!')
              return redirect('signup')
           else:
               user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
               user.save()
       else:
           messages.info(request,'Password does not match!!!')
           print("Password does not match!!!")
           return redirect('signup')
       return redirect('login')
    else:
        return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
       
       username=request.POST['username']
       password=request.POST['password1']
       user=auth.authenticate(username=username,password=password)
       
       if user is not None:
               auth.login(request,user)
               messages.info(request,f'Welcome {username}')
               return redirect('about')
       else:
           messages.info(request,'Invalid Username or Password.Try Again.')
           return redirect('login')
    else:
        messages.info(request,'Oops,Something went wrong.')
        return redirect('login')
def logout(request):
    auth.logout(request)
    return redirect('home')