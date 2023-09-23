from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from . import views

urlpatterns = [
    path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
