from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")
def blogs(request):
    return render(request,"blogs.html")
def login(request):
    return render(request,"login.html")
def single_page(request):
    return render(request,"single.html")
def success_page(request):
    return HttpResponse("<h1>Hey! this is a success page.</h1>")

# Create your views here.
