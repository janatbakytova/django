from cgitb import lookup
from shutil import register_unpack_format
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import ToDoListItem
# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductSerializer
from .models import Product

def welcome(request):
    return HttpResponse("<h1>Let`s work together!</h1>")
    

def todoapp_view(request):
    all_items = ToDoListItem.objects.all()
    return render(request, 'index.html', {'items': all_items})

def add_item(request):
    x = request.POST['content']
    new_item = ToDoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect("/")

def delete_item(request, id):
    item = ToDoListItem.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect("/")

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'




