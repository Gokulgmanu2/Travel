from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':

        username=request.POST['username']
        a=request.POST['first_name']
        b=request.POST['last_name']
        mail_id=request.POST['email']
        password=request.POST['password']
        conf_password=request.POST['password1']
        if password==conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")
            elif User.objects.filter(email=mail_id).exists():
                messages.info(request,"Email id already registered")
                return redirect("register")
            else:

                user=User.objects.create_user(username=username,first_name=a,last_name=b,email=mail_id,password=password)
                user.save();
                return redirect('login')
            print('user created')
        else:
            messages.info(request,"Password not matched")
            return redirect("register")
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')