from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name= models.CharField(max_length=200)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    slug = models.SlugField()
    decription = models.TextField()
    image = models.ImageField()
    price = models.FloatField(null=True ,blank=True)
    discount_price = models.FloatField(null=True,blank=True)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
