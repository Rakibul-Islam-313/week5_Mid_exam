from django.db import models
from car_categories.models import Brand
from django.contrib.auth.models import User 
# Create your models here.

class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_price = models.DecimalField(max_digits= 10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to ='media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.car_name
    
class Comment(models.Model):
    post = models.ForeignKey(Cars, on_delete = models.CASCADE, related_name = "comments")
    name =  models.CharField(max_length = 50)
    email  = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"comment by{self.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Cars, on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.car.car_name}"