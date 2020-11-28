from django.urls import path
from .views import uploadDocx
from .views import JsonTable
from .views import XMLTable

urlpatterns = [
    path('', uploadDocx, name='uploadDocx'),
    path('JsonTable', JsonTable, name='JsonTable'),
    path('XMLTable', XMLTable, name='XMLTable'),
        
]
