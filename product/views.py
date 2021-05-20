from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    # API endpoint that allows product to be viewed.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Product by pk.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer