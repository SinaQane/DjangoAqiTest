from django.urls import path
from . import views #. means current dir

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),

]
