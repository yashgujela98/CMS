from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from cmsapp.forms import SignUpForm,LoginForm
from cmsapp.models import Product
from django.contrib.auth.models import User, auth

# Create your views here.
def base(reqeust):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def login(request):
    if request.method=='POST':
        logfm=LoginForm(request=request,data=request.POST)
        if logfm.is_valid():
            uname=logfm.cleaned_data.get('username')
            upass=logfm.cleaned_data.get('password')
            user = authenticate(request=request, username=uname, password=upass)
            if user is not None:
                auth.login(request, user)
                return redirect('/home')
            else:
                logfm.add_error(None, "Invalid username or password.")

    else:
        logfm=LoginForm()
        
    return render(request,'login.html', {'form':LoginForm})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            auth_user = form.save()
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request,'signup.html', {'form': form})

def product(request):
    p=Product.objects.all()
    content={}
    content['data']=p 
    return render(request,'product.html',content)

def logout(request):
    auth.logout(request)
    return redirect('/login')
'''
def productform(request):
    if request.method=='POST':
        fmdata=Product(request.POST)
        return HttpResponse("CHECK TERMINAL")

    else:

        fm=Product()
        content={}
        content['mformdata']=fm
        return render(request,'productform.html',content)
'''
