from django.urls import path
from . import views

urlpatterns = [
    path("aluno/", views.index, name = "index")
]