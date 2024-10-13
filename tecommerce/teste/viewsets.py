from rest_framework import viewsets, permissions

from teste import serializers
from teste.filters import ClientFilter, ProductFilter, EmployeeFilter, SaleFilter
from teste.models import Client, Product, Employee, Sale


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filterset_class = ClientFilter
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = ProductFilter
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_class = EmployeeFilter
    permission_classes = [permissions.IsAuthenticated]


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    filterset_class = SaleFilter
    permission_classes = [permissions.IsAuthenticated]
