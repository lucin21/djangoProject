from django.contrib import admin
from products.models import Products



class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'numero_parte',
        'titulo',
        'categoria',
        'precio',
    )
    #

    #
    search_fields = ('numero_parte','titulo','categoria',)
    list_filter = ('categoria',)
    #
admin.site.register(Products, ProductsAdmin)