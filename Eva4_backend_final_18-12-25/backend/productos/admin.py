from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio','descripcion','imagen','categoria']
    list_display_links = ['titulo']