from django_filters import FilterSet, NumberFilter

from apps.models import Product


class ProductPriceFilterSet(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []
