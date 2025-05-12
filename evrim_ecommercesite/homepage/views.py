from django.shortcuts import render
from product.models import Product, Category


def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all()[:4]
    about_us_content = "Evrim, Hatay’ın Altınözü ilçesinde köy hayatı sürdüren, 30 yılı aşkın çiftçilik deneyimine sahip bir kadındır. " \
    "Doğayla iç içe yetiştirdiği organik ürünleri, hijyen ve kaliteye özen göstererek, kendi elleriyle hazırlamaktadır. " \
    "Evrim’in mutfağında her şey doğal ve sağlıklıdır; zeytinyağından salçaya, baharatlardan reçellere kadar geniş bir ürün yelpazesi sunar. " \
    "“Evimizden, Sofranıza!” sloganı ile geleneksel tarifleri yaşatırken, doğallığı ve sağlığı sofralarınıza taşır."
    return render(request, "homepage/homepage.html", {
        "categories": categories,
        "featured_products": featured_products,
        "about_us_content": about_us_content, 
    })

