from django.urls import path

from master_data.views.accounts import AccountDetailView
from master_data.views.accounts import AccountListCreateView
from master_data.views.cities import CityDetailView
from master_data.views.cities import CityListCreateView
from master_data.views.countries import CountryDetailView
from master_data.views.countries import CountryListCreateView
from master_data.views.product_categories import ProductCategoryDetailView
from master_data.views.product_categories import ProductCategoryListCreateView
from master_data.views.regions import RegionDetailView
from master_data.views.regions import RegionListCreateView
from master_data.views.sales import SalesDetailView
from master_data.views.sales import SalesListCreateView
from master_data.views.suppliers import SupplierDetailView
from master_data.views.suppliers import SupplierListCreateView
from master_data.views.warehouses import WarehouseDetailView
from master_data.views.warehouses import WarehouseListCreateView

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

    # Warehouse URLs
    path("warehouses/", WarehouseListCreateView.as_view(), name="warehouse-list"),
    path("warehouses/<int:pk>/", WarehouseDetailView.as_view(), name="warehouse-detail"),

    # Country URLs
    path("countries/", CountryListCreateView.as_view(), name="country-list"),
    path("countries/<int:pk>/", CountryDetailView.as_view(), name="country-detail"),

    # City URLs
    path("cities/", CityListCreateView.as_view(), name="city-list"),
    path("cities/<int:pk>/", CityDetailView.as_view(), name="city-detail"),

    # Region URLs
    path("regions/", RegionListCreateView.as_view(), name="region-list"),
    path("regions/<int:pk>/", RegionDetailView.as_view(), name="region-detail"),

    # Sales URLs
    path("sales/", SalesListCreateView.as_view(), name="sales-list"),
    path("sales/<int:pk>/", SalesDetailView.as_view(), name="sales-detail"),
]
