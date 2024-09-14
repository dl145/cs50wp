from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dominik", views.dominik, name="dominik"),
    path("<str:name>", views.greet, name="greet")
]