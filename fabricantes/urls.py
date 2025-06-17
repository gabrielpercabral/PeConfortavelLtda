from django.urls import path
from . import views

urlpatterns = [
    path("fabricantes/", views.index, name = "index")
]