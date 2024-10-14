from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        null=False,
    )

    activate = models.BooleanField(
        db_column='activate',
        default=False,
        null=False,
    )

    created_at = models.DateTimeField(
        db_column='created_at',
        auto_now_add=True,
        null=False,
    )

    modified_at = models.DateTimeField(
        db_column='modified_at',
        auto_now=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Client(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False,
    )

    age = models.IntegerField(
        db_column='age',
        null=False,
    )

    rg = models.CharField(
        db_column='rg',
        max_length=12,
        null=False,
    )

    cpf = models.CharField(
        db_column='cpf',
        max_length=12,
        null=False,
    )


class Product(ModelBase):
    description = models.CharField(
        db_column='description',
        max_length=100,
        null=False,
    )
    quantity = models.IntegerField(
        db_column='quantity',
        null=False,
    )


class Employee(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=70,
        null=False,
    )

    registration = models.CharField(
        db_column='registration',
        max_length=15,
        null=False,
    )


class Sale(ModelBase):
    id_client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.DO_NOTHING,
    )

    id_product = models.ForeignKey(
        Product,
        db_column='id_product',
        null=False,
        on_delete=models.DO_NOTHING,
    )

    id_employee = models.ForeignKey(
        Employee,
        db_column='id_employee',
        null=False,
        on_delete=models.DO_NOTHING,
    )

    nrf = models.CharField(
        db_column='nrf',
        max_length=255,
        null=False,
    )
