from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<h1> My second app </h1>")
def users(request):

    user_list = User.objects.order_by('first_name')
    context_dict = {"users":user_list}
    return render(request, "AppTwo/users.html",context=context_dict)
