from django.db import models

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='Product_image')

    def __str__(self):
        return self.name
    

class Collection(models.Model):

    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='Product_image')
    name1=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Shopping(models.Model):

    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='Product_image')

    def __str__(self):
        return self.name
    
    

class form(models.Model):

    name = models.CharField(max_length=20)
    message =models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    