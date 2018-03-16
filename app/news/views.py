# encode = utf-8
# user/bin/python3

from django.shortcuts import HttpResponse, render
from news.models import Teste


"""
Função: index()
Objetivo:
@method: get
Parâmetro: Sem parâmetros
"""
def index(request):
    context = {'title': 'Django E-Commerce'}
    return render(request, "home/index.html", context)


"""
Função: index()
Objetivo:
@method: get
Parâmetro: Sem parâmetros
"""
def products(request):
    context = {'title': 'Django E-Commerce'}
    return render(request, "products/products.html", context)


"""
Função: index()
Objetivo:
@method: get
Parâmetro: Sem parâmetros
"""
def get(request):
    post = int(request.GET.get('id'))
    return HttpResponse("Ola Devops %d" %post)


"""
Função: index() 
Objetivo:
@method: get
Parâmetro: Sem parâmetros
"""
def post(request):
    post = request.POST.get('name')
    return HttpResponse("Ola Devops %s" %post)


"""
Função: index()
Objetivo:
@method: get
Parâmetro: Sem parâmetros
"""
def teste(request):
    user = Teste.objects.all
    context = {'users': user, 'title': 'home' }
    return render(request, 'teste/teste.html', context)