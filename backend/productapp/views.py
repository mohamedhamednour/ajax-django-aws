from django.shortcuts import render
from rest_framework import filters, mixins, viewsets, status
from . import serializers, models, filters

# Create your views here.


class SubCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SubCategorySerializer
    queryset = models.SubCategory.objects.all().get_info()
    filterset_class = filters.SubCategoryFilter


class CategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
