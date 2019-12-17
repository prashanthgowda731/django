from django.urls import path
from app import views

app_name="myapp"
urlpatterns = [
    path('',views.home,name="home"),
    path('belur/',views.home1,name="home1"),
    path('halebidu/',views.home2,name="home2"),
]