from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from AppTwo.models import User
from AppTwo.forms import UserForm

# Create your views here.
def index(request):
    return HttpResponse("<h1> My second app </h1>")
def thanks(request):
    return render(request, "AppTwo/thanks.html")
def users(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            print("Validated")
            form.save()
            print("Saved")
            return HttpResponseRedirect(reverse("thanks"))

    return render(request, "AppTwo/users.html", {"modelform": form})
