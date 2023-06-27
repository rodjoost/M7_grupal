from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('producto/', views.producto, name="producto"),
    path('proveedor/', views.proveedor, name="proveedor"),
    path('pedido/', views.pedido, name="pedido"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register_user', views.register_user, name="register_user"),
]

