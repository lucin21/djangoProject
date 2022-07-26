from urllib import request
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductSerializer

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Products
from django.db.models import Q


class HomePage(TemplateView):
    template_name = 'index.html'


# class ProductsListViewCategoria(ListView):
#     template_name = 'resultados.html'
#     model = Products
#     paginate_by = 12
#     context_object_name = 'lista'
#
#     def get_queryset(self):
#         categoria = self.kwargs['categoria']
#         lista = Products.objects.filter(categoria=categoria)
#         return lista


class ProductsListViewBuscador(ListView):
    context_object_name = 'lista_libros'
    template_name = 'resultados.html'
    paginate_by = 12

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Products.objects.buscar_producto(palabra_clave)


class ApiProduct(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


