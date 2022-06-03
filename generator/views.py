from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def  home(request):
    return render(request, 'generator/home.html')

def password(request):

    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('Special'):
        characters.extend(list('!@£$%^&*()'))
    
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html',{'password':password})

def about (request):
    return render(request, 'generator/about.html')