from django.shortcuts import render
from Users.forms import CustomerForm, CustomerComplainForm, StudentForm

# Create your views here.
def Home(request):
    form = CustomerComplainForm()
    return render(request, 'Home.html',{'form':form})
def Login(request):
    return render(request, 'Login.html')
def Register(request):
    form = RegisterForm()
    return render(request, 'Register.html',{'form':form})
def Aboutus(request):
    return render(request, 'Aboutus.html')
def Gallery(request):
    return render(request, 'Gallery.html')
def Logout(request):
    form = CustomerForm()
    return render(request, 'Logout.html',{'form':CustomerForm})

