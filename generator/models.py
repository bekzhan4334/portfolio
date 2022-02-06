from django.db import models

class Info(models.Model):
    FIO = models.CharField(max_length=100)
    INN = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    orhan = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)



