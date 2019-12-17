from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"s.html")

def home1(request):
    return render(request,"s1.html")