from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantily', 'created_at', 'update_at',)
    search_fields = ('product__title',)


admin.site.register(models.Outflow, OutflowAdmin)
