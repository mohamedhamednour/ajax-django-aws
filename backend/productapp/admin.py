from django.contrib import admin

# Register your models here.

from .models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("id",)
    list_per_page = 10
    list_editable = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name",)
    list_filter = ("category",)
    ordering = ("id",)
    list_per_page = 10
    list_editable = ("name",)
