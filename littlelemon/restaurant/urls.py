from django.contrib import admin 
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
    path('about/', views.about, name="about"),
    path('menu/', views.Menu, name="menu"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    # API paths
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
]
