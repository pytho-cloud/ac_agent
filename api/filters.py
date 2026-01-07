# filters.py
import django_filters
from .models import AC ,Review

class ACFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = AC
        fields = [
            'condition',
            'brand',
            'ac_type',
            'capacity',
            'energy_rating',
            'ton'
        ]



class ReviewFilter(django_filters.FilterSet):
    min_star = django_filters.NumberFilter(field_name='star', lookup_expr='gte')
    max_star = django_filters.NumberFilter(field_name='star', lookup_expr='lte')

    class Meta:
        model = Review
        fields = ['product_name']
