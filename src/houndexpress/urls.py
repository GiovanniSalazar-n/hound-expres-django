from django.urls import path

from houndexpress import views

urlpatterns = [
    path("", views.home, name="home"),
]
