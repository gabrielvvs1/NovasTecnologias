from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html') 

def contato(request):
    return HttpResponse('Contato: <br> Telefone:4002-8922 <br> Email: gabrielvvs123@gmail.com' )

