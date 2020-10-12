from django.shortcuts import render
from django.http import HttpResponse
import random, string

# Password generator
def home(request):
    return render(request,'generator/home.html')

def password(request):

    character = list(string.ascii_lowercase)

    if request.GET.get('Uppercase'):
        character.extend(list(string.ascii_uppercase))
    if request.GET.get('Special Character'):
        character.extend(list(string.punctuation))
    if request.GET.get('Number'):
        character.extend(list('0123456789'))

    length = int(request.GET.get("length",32))
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html',{"password":thepassword},)

def about(request):
    return render(request,'generator/about.html')
    