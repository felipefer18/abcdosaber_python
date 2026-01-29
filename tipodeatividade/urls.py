from django.urls import path
from tipodeatividade import views

urlpatterns = [
    path("", views.index, name="index"),
    path("i2/", views.index2, name="index2")
   
]