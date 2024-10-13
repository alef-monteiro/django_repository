from django_filters import rest_framework as filters
from teste.models import Client, Product, Employee, Sale

# Search Filters
LIKE = 'icontains'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
IN = 'in'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'


class ClientFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id', lookup_expr=EQUALS)
    name = filters.CharFilter(field_name='name', lookup_expr=LIKE)
    age = filters.CharFilter(field_name='age', lookup_expr=EQUALS)
    cpf_sw = filters.CharFilter(field_name='cpf', lookup_expr=STARTS_WITH)
    cpf_eq = filters.CharFilter(field_name='cpf', lookup_expr=EQUALS)
    rg_sw = filters.CharFilter(field_name='rg', lookup_expr=STARTS_WITH)
    rg_eq = filters.CharFilter(field_name='rg', lookup_expr=EQUALS)

    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf', 'rg', 'age']


class ProductFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id', lookup_expr=EQUALS)
    description = filters.CharFilter(field_name='description', lookup_expr=LIKE)
    quantity = filters.CharFilter(field_name='quantity', lookup_expr=EQUALS)

    class Meta:
        model = Product
        fields = ['id', 'description', 'quantity']


class EmployeeFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id', lookup_expr=EQUALS)
    name = filters.CharFilter(field_name='name', lookup_expr=LIKE)
    registration_sw = filters.CharFilter(field_name='registration', lookup_expr=STARTS_WITH)
    registration_eq = filters.CharFilter(field_name='registration', lookup_expr=EQUALS)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'registration']


class SaleFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id', lookup_expr=EQUALS)
    id_client = filters.CharFilter(field_name='id_client', lookup_expr=EQUALS)
    id_product = filters.CharFilter(field_name='id_product', lookup_expr=EQUALS)
    id_employee = filters.CharFilter(field_name='id_employee', lookup_expr=EQUALS)
    nrf = filters.CharFilter(field_name='nrf', lookup_expr=EQUALS)

    class Meta:
        model = Sale
        fields = ['id', 'id_client', 'id_product', 'id_employee', 'nrf']
