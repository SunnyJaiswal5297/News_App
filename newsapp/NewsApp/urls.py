from django.urls import path
from .views import index,bbc

urlpatterns = [
    path('',index,name="index"),
    path('bbc/',bbc,name="bbc"),
]