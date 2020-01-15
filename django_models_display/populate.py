import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myapp.settings")

#setting up the django features
import django
django.setup()

from faker import Faker#get get the fake data
from myapp.models import *
import random #to choose data randomly

f=Faker()
topics=["Music","Sports","Social Media","Movies","News","Aggrigater","Educational"]
def add_topic(top_name):
    t=Topic.objects.get_or_create(top_name=top_name)[0]
    t.save()
    return t

def add_webpage(top_name,name,url):
    t=add_topic(top_name)
    w=Webpage.objects.get_or_create(top_name=t,name=name,url=url)[0]
    w.save()
    return w

def add_access_details(top_name,name,url,date):
    w=add_webpage(top_name,name,url)
    a=Access_Details.objects.get_or_create(name=w,date=date)[0]
    a.save()

def add_data():
    top_name=random.choice(topics)
    name=f.first_name()
    url=f.url()
    date=f.date()
    add_access_details(top_name,name,url,date)

if __name__=="__main__":
    N=int(input("Enter the number of fake data that you wanted to populate "))
    for i in range(N):
        add_data()