from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('add_number/', views.add_number)
]