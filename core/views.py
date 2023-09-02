from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request,'Dashboard.html')

def manage(request):
    
    return render(request,'manage.html')

def orders(request):
    
    return render(request,'orders.html')

def profile(request):
    
    return render(request,'profile.html')

def contact(request):
    
    return render(request,'contact.html')

def logout(request):
    
    return render(request,'Logout.html')

def vendors(request):
    
    return render(request,'vendors.html')


