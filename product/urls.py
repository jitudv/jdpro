from django.urls import path
from .views import hello_view
from . import views

urlpatterns = [
    path('demo/', hello_view, name='index_view'),
    path('demo1/', views.hello_view, name='view_home'),
    path('index', views.index, name='index'),
]
