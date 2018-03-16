# user/bin/python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'web_site/index.html')


def product(request):
    return render(request, 'web_site/product.html')


def products_list(request):
    return render(request, 'web_site/products_list.html')


def contact(request):
    return render(request, 'web_site/contact.html')