from django.shortcuts import render

# Create your views here.
def home(request):
    l=["a","b","add","prashanth","peace","new"]
    return render(request,"s.html",context={"d":10,"h":l})