from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("subcategories", views.SubCategoryViewset, basename="subcategory")
router.register("categories", views.CategoryViewset, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]
