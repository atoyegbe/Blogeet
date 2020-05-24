import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class blogFilter(django_filters.FilterSet):
    search = CharFilter(field_name='title', lookup_expr='icontains');
    