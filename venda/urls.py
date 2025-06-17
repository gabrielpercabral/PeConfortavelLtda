from django.urls import path
from . import views

urlpatterns = [
    path("venda/", views.index, name = "index")
]