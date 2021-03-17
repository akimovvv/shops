from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(verbose_name="Category", max_length=200)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(verbose_name='Maker', max_length=200)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('makerview', kwargs={'slug': self.slug})




class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Product`s category', on_delete=models.CASCADE)
    maker = models.ForeignKey(Maker, verbose_name='Maker', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=250, unique=True)
    price = models.DecimalField(verbose_name='Price', max_digits=9, decimal_places=2)
    description = models.TextField(verbose_name='description')
    img = models.ImageField(verbose_name='Image')
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name