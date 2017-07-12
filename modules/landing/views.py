from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import LoginForm,SignupForm
# Create your views here.


def index(request):
    return render(request,'landing/index.html')

def SignUp(request):

    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.cleaned_data.pop('confirm_password',None)
            print(form.cleaned_data)
            user = User.objects.create_user(**form.cleaned_data)
            return redirect('landing:index')
    
    else:
        return render(request,'landing/signup.html',{'form':form})

def Login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('landing:index')
            else:
                return HttpResponse("El usuario no exite en la BD")
    else:
        return render(request,'landing/login.html',{'form':form})
