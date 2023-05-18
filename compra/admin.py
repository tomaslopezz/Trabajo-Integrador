from django.contrib import admin
from .models import Producto, Proveedor

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'proveedor', 'stock_actual']
    
    list_filter = ['nombre', 'proveedor']

    search_fields = ['nombre']


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']
    
    list_filter = ['apellido']

    search_fields = ['nombre', 'apellido']




admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)

