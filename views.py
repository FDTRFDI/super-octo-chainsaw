from django.shortcuts import render 
from django.http import HttpResponseRedirect 
from .forms import *
from .models import *
# Create your views here.

def new_register(request):
    if (request.method == 'POST'): 
        form=RegistreForm(request.POST) 
        if (form.is_valid()):

         down=form.cleaned_data['first_name']
         okay= Register.objects.create(first_name=down,last_name=down,
          email=down,address=down ,phone=down ,password=down,des=down)

         okay.save()
    form=RegistreForm()     
    return render(request,'register.html',{'form':form})       

def new_login(request):
    if (request.method == 'POST'): 
        form= LoginForm(request.POST) 
        if (form.is_valid()):

         goole=form.cleaned_data['name']
         dd=Login.objects.create(name=goole,)
         dd.save()
    form=LoginForm()     
    return render(request,'login.html',{'form':form})






def home(request):
    return render(request,'home.html')


def aboutus(request):
    return render(request,'aboutus.html')


def header(request):
    return render(request,'header.html')


def footer(request):
    return render(request,'footer.html')


def contact(request):
    return render(request,'contact.html')


def navbar (request):
    return render(request,'navbar.html')


