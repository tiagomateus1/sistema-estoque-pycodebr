from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowsListView.as_view(), name='inflows_list'),
    path('inflows/create/', views.InflowsCreateView.as_view(), name='inflows_create'),
    path('inflows/<int:pk>/detail/', views.InflowsDetailView.as_view(), name='inflows_detail'),
]
