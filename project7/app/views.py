from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"s.html")

def page1(request):
    return render(request,"s1.html")

def page2(request):
    return render(request,"s2.html")

