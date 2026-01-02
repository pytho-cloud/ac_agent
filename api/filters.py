# filters.py
import django_filters
from .models import AC

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
        ]
