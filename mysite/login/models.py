from django.db import models
from datetime import datetime
from company.models import Product
from django.urls import reverse


class Register(models.Model):
    Fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    register_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to="user/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.Fullname


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    customer = models.ForeignKey(Register, on_delete=models.CASCADE, default=None)
    Quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    def update(self):
        return reverse('login:update', args=[self.id])

    def deleteQuery(self):
        return reverse('login:delete', args=[self.id])

    def checkout(self):
        return reverse('login:checkout')

class Bill(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.id)

class Log(models.Model):
    bill_id = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    Quantity = models.IntegerField(default=1)

