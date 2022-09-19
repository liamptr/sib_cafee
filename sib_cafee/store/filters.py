from django_filters.rest_framework import FilterSet
from .models import Food

class FoodFilter(FilterSet):
  class Meta:
    model = Food
    fields = {
      'collection_id': ['exact'],
      'unit_price': ['gt', 'lt']
    }