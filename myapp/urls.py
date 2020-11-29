from django.urls import path
from .views import uploadDocx
from .views import JsonTable
from .views import XMLTable
from .views import Home
from .views import editTable

urlpatterns = [
    path('uploadDocx', uploadDocx, name='uploadDocx'),
    path('JsonTable', JsonTable, name='JsonTable'),
    path('XMLTable', XMLTable, name='XMLTable'),
    path('home', Home, name='home'),
    path('editTable', editTable, name='editTable'),
        
]
