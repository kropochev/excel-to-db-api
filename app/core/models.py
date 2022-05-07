from django.db import models


class Upload(models.Model):
    bills_file = models.FileField()
    clients_file = models.FileField()


class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    client_name = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bill(models.Model):
    client_org = models.ForeignKey('Organization', on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField()
    sum = models.IntegerField()
