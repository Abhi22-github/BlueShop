from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('explore', views.explore_all, name='explore-all'),
    path('product/<int:id>/', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('orders', views.orders, name='orders'),
]