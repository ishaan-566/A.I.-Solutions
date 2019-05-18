from django.db import models
from login.models import Register, Product
from django.urls import reverse

class Stocks(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

    def remove(self):
        return reverse('inventory:remove_stock', args=[self.id, 'remove'])
    def add(self):
        return reverse('inventory:remove_stock', args=[self.id, 'add'])
    def dele(self):
        return reverse('inventory:delete_stock', args=[self.id])


class LogInventory(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    operation = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)