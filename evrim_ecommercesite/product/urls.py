from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_view, name="product"),
    path("category/<slug:slug>", views.product_by_category, name="product_by_category"),
    path("product/<slug:slug>", views.product_detail, name="product_detail"),
    path('products/amount/<str:unit>/<int:quantity>/', views.product_by_quantity, name='product_by_quantity'),
]