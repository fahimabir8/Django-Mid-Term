from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User 

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE , null=True, blank = True)
    image = models.ImageField(upload_to='static/car-media/',blank=True, null=True )
        
    def __str__(self):
        return self.name 
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    area = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'comment by {self.name}'
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='purchases')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Purchased by :- {self.user.username}'
