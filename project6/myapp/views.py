from django.shortcuts import render

# Create your views here.
def demo(request):
    return render (request,"s.html")
def demo1(request):
        return render (request,"s1.html")
