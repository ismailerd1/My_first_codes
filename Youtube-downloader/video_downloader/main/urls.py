from django.urls import path
from .views import index, download_details

urlpatterns = [
    path('', index, name='index'),
    path('download_details/', download_details, name='download_details'),
]