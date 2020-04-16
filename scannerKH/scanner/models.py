from django.db import models
from django.core.validators import int_list_validator


class FTP(models.Model):
    host = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Wholesaler(models.Model):
    name = models.CharField(max_length=50)
    ftp = models.ForeignKey(FTP, on_delete=models.CASCADE)

class Order(models.Model):
    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.PROTECT)
    create_stamp = models.DateTimeField('date created')
    modified_stamp = models.DateTimeField('date modified', auto_now=True)
    transmit_stamp = models.DateTimeField('date transmitted', blank=True, null=True)
    articles = models.CharField(validators=[int_list_validator], max_length=100000)
