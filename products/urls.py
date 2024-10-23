from django.urls import path
from . import views


urlpatterns = [
    path('products/list/', views.ProductsListView.as_view(), name='products_list'),
    path('products/create/', views.ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/detail/', views.ProductsDetailView.as_view(), name='products_detail'),
    path('products/<int:pk>/update/', views.ProductsUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', views.ProductsDeleteView.as_view(), name='products_delete'),
]
