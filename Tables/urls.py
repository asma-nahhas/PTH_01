from django.urls import path
from .views import Tables
from . import views

urlpatterns = [
    path('Tables/', Tables, name='Tables'),
    #path('JsonTable', JsonTable, name='JsonTable'),
    path('XMLTable/', views.XMLTable, name='XMLTable')
    
    
]
