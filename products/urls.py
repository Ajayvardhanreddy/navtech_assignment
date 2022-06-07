from django.urls import path
from . import views

urlpatterns = [
    path('user_create_order/', views.user_create_order),
    path('admin_create_order/', views.admin_create_order),
    path('admin_get_orders/', views.admin_get_orders),
]
