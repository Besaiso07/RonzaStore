from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_html, name='store_html'),
    path('store/category/<slug:category_slug>/', views.store_html, name='product_by_category'),
    path('store/category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('store/search/', views.search, name='search'),
]
