from django.urls import path, include
from django.contrib import admin
from products import views

urlpatterns = [
    path('product/<product_id>/', views.product, name='product'),
]