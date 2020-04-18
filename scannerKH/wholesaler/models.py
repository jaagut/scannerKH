from django.db import models

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
