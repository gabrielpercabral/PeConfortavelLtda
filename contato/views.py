from django.shortcuts import render

# Create your views here.

def contatos(request):
    return render(request,'contato/contatos.html')
