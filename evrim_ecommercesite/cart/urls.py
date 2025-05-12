from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("", views.cart_detail, name="cart_detail"),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('update/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]