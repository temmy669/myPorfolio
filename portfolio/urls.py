from django.urls import path
from . import views

urlpatterns = [
    path('port/', views.index, name = 'index'),
]