from django.urls import reverse
from django.db import models

from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="photos/products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        return reverse("product_detail", args=(self.category.slug, self.slug))
