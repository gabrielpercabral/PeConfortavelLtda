from django.shortcuts import render

def contatos(request):
    return render(request, 'contato/index.html')
