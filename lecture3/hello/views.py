from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def dominik(request):
    return HttpResponse("Hello, Dominik!")

def greet(request, name):
    return render(request, "hello/greet.hmtl", {
        "name": name.capitalize()
    })