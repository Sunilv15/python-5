from django.shortcuts import render,httpResponse

# Create your views here.


def index(request):
    return HttpResponse("hello from django server!!!")

def contact(request):
    return HttpResponse("contact page")