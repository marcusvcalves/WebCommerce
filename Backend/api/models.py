from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='files/products/images', null=True, blank=True)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    
    def __str__(self):
        return self.product.name
    
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
        
    def __str__(self):
        return self.product.name

