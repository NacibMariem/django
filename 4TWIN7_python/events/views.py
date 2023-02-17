from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#tjr on a du requetes 
def homePage(Request): #esm l fonction dima yabda bel miniscule
    return HttpResponse('<h1>Titlr here</h1>') #pour renvoyer un HTML on appel HTMLResponse