from django.shortcuts import render
from shop.models import *

# Create your views here.

def getCategory():
    return Category.objects.all()

def homePage(req):
    data ={}
    data['products']= Product.objects.all()
    data['category'] = getCategory()
    return render(req,'home.html',data)

def filterCat(req,slug):
    data ={}
    data['products']= Product.objects.filter(category__slug = slug)
    data['category'] = getCategory()
    return render(req,'home.html',data)

def search(req):
    search = req.GET.get('search')
    data ={}
    data['products']= Product.objects.filter(name__contains = search)
    data['category'] = getCategory()
    return render(req,'home.html',data)