from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Car_Detail(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='showroom/car_images/upload',  blank = True, null = True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    car = models.ForeignKey(Car_Detail, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name