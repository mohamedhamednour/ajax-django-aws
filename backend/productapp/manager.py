from django.db import models
from django.db.models import F


class SubCategoryuerySet(models.QuerySet):
    def get_name_category(self):
        return self.annotate(name_category=F("category__name"))

    def get_all_related(self):
        return self.select_related("category").prefetch_related("parent")

    def get_info(self):
        return self.get_name_category().get_all_related()
