import string
from string import ascii_lowercase
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html") 


def password(request):

    # characters = list('abcdefghijklmnopqrstuvwxyz')
    characters = list(string.ascii_lowercase)

    if request.GET.get("uppercase"):
        characters.extend(list(string.ascii_uppercase))

    length  = int(request.GET.get('length', 10))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_-+="))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password':thepassword})


def about(request):
    return render(request, "generator/about.html")