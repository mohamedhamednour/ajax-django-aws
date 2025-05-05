from django.db import models

from . import manager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subcategories_child",
        on_delete=models.CASCADE,
    )
    objects = manager.SubCategoryuerySet.as_manager()

    def __str__(self):
        return self.name
