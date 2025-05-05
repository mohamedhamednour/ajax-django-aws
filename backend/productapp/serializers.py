from rest_framework import serializers


from .models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    name_category = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = ["id", "name", "name_category"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
