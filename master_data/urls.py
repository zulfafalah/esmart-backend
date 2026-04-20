from django.urls import path

from master_data.views.accounts import AccountDetailView
from master_data.views.accounts import AccountListCreateView
from master_data.views.product_categories import ProductCategoryDetailView
from master_data.views.product_categories import ProductCategoryListCreateView
from master_data.views.suppliers import SupplierDetailView
from master_data.views.suppliers import SupplierListCreateView

app_name = "master_data"

urlpatterns = [
    # Product Category URLs
    path("product-category/", ProductCategoryListCreateView.as_view(), name="product-category-list"),
    path("product-category/<int:pk>/", ProductCategoryDetailView.as_view(), name="product-category-detail"),
    
    # Account URLs
    path("accounts/", AccountListCreateView.as_view(), name="account-list"),
    path("accounts/<int:pk>/", AccountDetailView.as_view(), name="account-detail"),

    # Supplier URLs
    path("suppliers/", SupplierListCreateView.as_view(), name="supplier-list"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
]
