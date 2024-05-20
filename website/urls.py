from django.urls import path
from . import views

urlpatterns = [
    path('', views.contDB, name='contents'),
    path('gallery/', views.galleryDB, name='gallery'),
]