from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> My second app </h1>")
def help(request):
    context_ = {"error":"The problem is the internet"}
    return render(request, "AppTwo/help.html",context=context_)
