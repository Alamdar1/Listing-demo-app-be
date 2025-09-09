import django_filters
from .models import List

class ListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = List
        fields = ['title']
