from django.urls import path
from . import views

urlpatterns = [
    path('', views.ide_home, name='ide_home'),
    path('compile/', views.compile_code, name='compile_code'),
]
