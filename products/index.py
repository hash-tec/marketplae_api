from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product


@register(Product)
class ProductSearchIndex(AlgoliaIndex):
    fields = ('product_name', 'brand', 'description', 'size', 
              'discount_percentage', 'category', 'slug')