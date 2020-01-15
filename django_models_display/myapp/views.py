from django.shortcuts import render
from myapp.models import*
# Create your views here.
def topic_form (request):
    topics=Topic.objects.all()
    if request.method=="POST":
        topic=request.POST.get("top")
        web_data=Webpage.objects.filter(top_name=topic)
        return  render(request,"web.html",context={"webpages":web_data})
    return render(request,"form_demo.html",context={"topics":topics})