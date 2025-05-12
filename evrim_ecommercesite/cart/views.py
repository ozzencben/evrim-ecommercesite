from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Kullanıcının sepete ait kayıtları al ya da yeni oluştur
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Eğer ürün zaten sepette varsa, adedi artır
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect("cart_detail")


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product")

    total_price = 0
    for item in items:
        item.total_price = item.product.price * item.quantity  # Ara toplam hesaplama
        total_price += item.total_price  # Toplam fiyatı güncelleme

    return render(request, 'cart/cart_detail.html', {
        'cart_items': items,
        'total_price': total_price,
    })


@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    return redirect("cart_detail")


def update_cart_quantity(request, product_id, action):
    # Kullanıcının sepetini al
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    if action == 'increase':
        cart_item.quantity += 1  # Miktarı artır
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1  # Miktarı azalt (1'den az olmasın)

    cart_item.save()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('cart_detail')