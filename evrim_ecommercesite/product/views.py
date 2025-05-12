from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {
        "product": product
    })

def product_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "product/product.html", {
        "products": products,
        "categories": categories
    })

def product_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, "product/product.html", {
        "selected_category": category,
        "products": products,
        "categories": categories
    })


def product_by_quantity(request, unit, quantity):
    products = Product.objects.filter(unit=unit, quantity=quantity)
    categories = Category.objects.all()
    selected_category = None
    selected_quantity = f"{quantity}{unit}" 

    return render(request, 'product/product.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'selected_quantity': selected_quantity
    })
