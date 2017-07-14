from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
#from django.contrib.auth.models import User
from modules.users.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm,SignupForm,ImageUploadForm
from .models import Images
import json
# Create your views here.


def index(request):
    imagenes = Images.objects.order_by('-fecha_creado')

    return render(request,'landing/index.html',{'img':imagenes})
@login_required
def Profile(request):
    imagenes = Images.objects.filter(usuario = request.user)
    return render(request,'landing/profile.html',{'img':imagenes})

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




def Logout(request):
    logout(request)
    return redirect('landing:index')

@login_required
def UploadImage(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)

        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.usuario = request.user
            imagen.save()

            return redirect('landing:index')
        else:
            return HttpResponse("Hay problemas en el Formulario")
    else:
        form = ImageUploadForm()

        return render(request,'landing/upload_form.html',{'form':form})



def ImagesEndpoint(request):
    
    imagenes = Images.objects.all()
    imgs = []
    for imagen in imagenes:
        imagen_dict = imagen.__dict__
        user_dict = imagen.usuario.__dict__
        user_dict.pop('_state',None)
        user_dict.pop('_usuario_cache',None)
        imagen_dict['usuario'] = user_dict
        imagen_dict.pop('_state',None)
        imagen_dict.pop('_usuario_cache',None)
        print(imagen_dict)
        imgs.append(imagen_dict)

    data = {
        "data":imgs
    } 

    return JsonResponse(data)

@csrf_exempt
def ImagesEndpointUpload(request):
    
    if request.method == "POST":
       
        print(request.POST['saludo'])
        data = {
            "mensaje":"Saludo recibido"
        }
        return JsonResponse(data)
