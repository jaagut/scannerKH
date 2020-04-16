from django.db import models
from django.core.validators import int_list_validator
from datetime import datetime


class FTP(models.Model):
    host = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"HOST: {self.host}, USER: {self.user}"

class Wholesaler(models.Model):
    name = models.CharField(max_length=50)
    ftp = models.ForeignKey(FTP, on_delete=models.CASCADE)

    def __str__(self):
        return f"NAME: {self.name}, FTP: ({self.ftp.__str__()})"

class Order(models.Model):
    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.PROTECT)
    create_stamp = models.DateTimeField('date created', default=datetime.now)
    modified_stamp = models.DateTimeField('date modified', auto_now=True)
    transmit_stamp = models.DateTimeField('date transmitted', blank=True, null=True)
    articles = models.CharField(validators=[int_list_validator], max_length=100000)

    def __str__(self):
        return f"WHOLESALER: ({self.wholesaler.__str__()}), CREATE: {self.create_stamp.__str__()}, MODIFIED: {self.modified_stamp.__str__()}, TRANSMITTED: {self.transmit_stamp.__str__()}\nARTICLES: [{self.articles}]"