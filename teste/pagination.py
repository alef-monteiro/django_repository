from rest_framework import pagination
from teste.models import Client

class ClientPagination(pagination.PageNumberPagination):
    pass