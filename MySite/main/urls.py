from django.urls import path
from . import views

#connect the view with the apk and creates a path    
urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create")
]