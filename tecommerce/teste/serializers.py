from rest_framework import serializers

from teste.models import Client, Product, Employee, Sale


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    age = serializers.IntegerField(min_value=0, max_value=100)
    cpf = serializers.CharField(min_length=11)
    rg = serializers.CharField(min_length=11)

    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    registration = serializers.CharField(max_length=70)

    class Meta:
        model = Employee
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    id_client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    id_product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    id_employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    nrf = serializers.IntegerField()

    class Meta:
        model = Sale
        fields = '__all__'
