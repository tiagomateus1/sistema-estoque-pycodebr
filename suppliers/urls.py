from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list/', views.SuppliersListView.as_view(), name='suppliers_list'),
    path('suppliers/create/', views.SuppliersCreateView.as_view(), name='suppliers_create'),
    path('suppliers/<int:pk>/detail/', views.SuppliersDetailView.as_view(), name='suppliers_detail'),
    path('suppliers/<int:pk>/update/', views.SuppliersUpdateView.as_view(), name='suppliers_update'),
    path('suppliers/<int:pk>/delete/', views.SuppliersDeleteView.as_view(), name='suppliers_delete'),
]
