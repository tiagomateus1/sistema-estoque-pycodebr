from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowsListView.as_view(), name='outflows_list'),
    path('outflows/create/', views.OutflowsCreateView.as_view(), name='outflows_create'),
    path('outflows/<int:pk>/detail/', views.OutflowsDetailView.as_view(), name='outflows_detail'),
]
