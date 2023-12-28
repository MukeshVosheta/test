from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")

def defo(request):
    return render(request,'base.html')