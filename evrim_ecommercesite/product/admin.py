from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Category, Product

class PriceRangeFilter(SimpleListFilter):
    title = 'Fiyat Aralığı'  # Başlık
    parameter_name = 'price'  # URL parametresi ismi

    def lookups(self, request, model_admin):
        # Fiyat aralığı seçenekleri
        return (
            ('less_than_100', '₺100 Altı'),
            ('between_100_and_1000', '₺100 - ₺1000 Arası'),
            ('greater_than_1000', '₺1000 Üstü'),
        )

    def queryset(self, request, queryset):
        # Fiyat filtresi
        if self.value() == 'less_than_100':
            return queryset.filter(price__lt=100)
        if self.value() == 'between_100_and_1000':
            return queryset.filter(price__gte=100, price__lte=1000)
        if self.value() == 'greater_than_1000':
            return queryset.filter(price__gt=1000)
        return queryset


class StockRangeFilter(SimpleListFilter):
    title = 'Stok Miktarı'  # Başlık
    parameter_name = 'stock'  # URL parametresi ismi

    def lookups(self, request, model_admin):
        # Stok aralığı seçenekleri
        return (
            ('low_stock', 'Az Stok (1-10)'),
            ('medium_stock', 'Orta Stok (11-50)'),
            ('high_stock', 'Yüksek Stok (50+)'),
        )

    def queryset(self, request, queryset):
        # Stok filtresi
        if self.value() == 'low_stock':
            return queryset.filter(stock__gte=1, stock__lte=10)
        if self.value() == 'medium_stock':
            return queryset.filter(stock__gte=11, stock__lte=50)
        if self.value() == 'high_stock':
            return queryset.filter(stock__gte=51)
        return queryset


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "unit", "quantity", "category", "created_at", "updated_at", "slug")
    list_filter = (
        "category", 
        "created_at", 
        PriceRangeFilter,  # Fiyat filtresi eklendi
        StockRangeFilter,  # Stok filtresi eklendi
    )
    search_fields = ("name", "description",)
    fields = (
        'name', 
        'description', 
        'price', 
        'stock', 
        'category', 
        'image', 
        'unit',  # Unit seçeneği eklendi
        'quantity',  # Quantity seçeneği eklendi
        'slug'
    ) 
    prepopulated_fields = {'slug': ('name',)}  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id",)
    list_filter = ("name",)
    search_fields = ("name",)
    fields = ("name", "slug")  

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
