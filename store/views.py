from django.shortcuts import get_object_or_404, render
from category.models import Category

from store.models import Product

# Create your views here.


def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    context = {
        "products": products,
        "product_count": products.count(),
    }
    return render(request, "store/store.html", context)


def product_detail(request, category_slug=None, product_slug=None):
    product = Product.objects.filter(
        category__slug=category_slug, slug=product_slug
    ).first()
    if not product:
        raise
    context = {
        "product": product,
    }
    return render(request, "store/product_detail.html", context)
