from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Lucas Ferreira',
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('sobre')
