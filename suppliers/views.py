from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class SuppliersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Suppliers
    template_name = 'supplier_list.html'
    context_object_name = 'supplier'
    paginate_by = 10
    permission_required = 'suppliers.view_suppliers'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset


class SuppliersCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Suppliers
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.add_suppliers'


class SuppliersDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Suppliers
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_suppliers'


class SuppliersUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Suppliers
    template_name = 'supplier_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.change_suppliers'


class SuppliersDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Suppliers
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('suppliers_list')
    permission_required = 'suppliers.delete_suppliers'
