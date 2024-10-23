from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class InflowsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflows_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        
        return queryset


class InflowsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    template_name = 'inflows_create.html'
    form_class = forms.InflowsForm
    success_url = reverse_lazy('inflows_list')
    permission_required = 'inflows.add_inflow'


class InflowsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflows_detail.html'
    permission_required = 'inflows.view_inflow'
