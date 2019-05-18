from django.db import models
from django.urls import reverse

class Company(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company:company_detail', args=[self.slug])

    def get_absolute_url_cat(self):
        return reverse('company:product_list_by_company', args=[self.slug])

    def inventory(self):
        return reverse('inventory:product_list_by_company', args=[self.slug])


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company:product_list_by_category', args=[self.slug])
    def inventory(self):
        return reverse('inventory:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=1500)
    available = models.BooleanField(blank=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company:product_detail', args=[self.id, self.slug])

    def add_cart(self):
        return reverse('company:add_cart', args=[self.slug, self.id])
    def add_stock(self):
        return reverse('inventory:add_stock', args=[self.id])
