from django.contrib import admin
from .models import Producto,Marca
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display=["id","nombre","precio","marca"]
    list_editable=["precio"]
    list_filter=["marca"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Marca)