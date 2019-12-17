from django.url import path
from app import views
app_name="app"

urlpatterns = [
    path("page1/",views.page1,name="page1"),
]
