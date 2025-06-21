from django.urls import path
from . import views

app_name = "contato"

urlpatterns = [
    path("contato/", views.contatos, name = "contatos")
]