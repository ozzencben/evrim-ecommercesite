from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    UNIT_CHOICES = [
        ('g', 'Gram'),
        ('ml', 'Mililitre'),
    ]

    QUANTITY_CHOICES = [
        (500, '500'),
        (1000, '1000'),
        (2500, '2500'),
        (5000, '5000'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/")
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='g')  # Varsayılan gram
    quantity = models.PositiveIntegerField(choices=QUANTITY_CHOICES, default=500)  # Varsayılan 500
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.quantity}{self.unit}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
