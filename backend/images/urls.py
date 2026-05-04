from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_img, name='upload'),
    path('get', views.get_img, name='get'),
    path('delete', views.delete_img, name='delete'),
    path('db', views.db_model, name='db'),
]
