from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos
# Create your views here.

def produtos(request):
    dados = Produtos.objects.all()
    return render(
        request,
        'ver_produto.html',
        {'dados':dados},        
                  )

# views.py
