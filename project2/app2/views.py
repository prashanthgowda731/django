from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse("<h1>hello how are you</h1>")
def home(request):
    return render(request,"sam2.html")
# Create your views here.
