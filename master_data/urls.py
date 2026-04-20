from django.urls import path

from master_data.views.product_categories import ProductCategoryDetailView
from master_data.views.product_categories import ProductCategoryListCreateView

app_name = "master_data"

urlpatterns = [
    # Product Category URLs
    path("product-category/", ProductCategoryListCreateView.as_view(), name="product-category-list"),
    path("product-category/<int:pk>/", ProductCategoryDetailView.as_view(), name="product-category-detail"),
]
