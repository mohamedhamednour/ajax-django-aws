from .models import SubCategory
from django_filters import rest_framework as filters


class SubCategoryFilter(filters.FilterSet):

    class Meta:
        model = SubCategory
        fields = ("category", "parent")
