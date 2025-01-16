from django.contrib import admin
from .models import Producto


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'categoria', 'name', 'mesure', 'quantity_un', 'cost_un', 'sale_price', 'date_created', 'description')
    search_fields = ['code', 'name']
    readonly_fields = ('date_created', 'date_modify')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Producto, ProductAdmin)
