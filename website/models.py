from django.db import models
from secrets import choice

# Create your models here.
class Content(models.Model):
    header = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=30, blank=False)
    message = models.TextField(max_length=300, blank=False)
    image = models.ImageField(upload_to='media/', blank=True)
    status = models.CharField(max_length=10, blank=True, null=True, default='num', choices=(
        ('active', 'active'),
        ('num', 'num'),
    ))
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # status

    def __str__(self):
        return self.message[0:70]

class Gallery(models.Model):
    header = models.CharField(max_length=20, blank=False)
    title = models.CharField(max_length=20, blank=False)
    message = models.TextField(max_length=200, blank=False)
    image = models.ImageField(upload_to='media/', blank=False, null=True)
    price = models.CharField(max_length=300, blank=False, null=True)
    rating = models.CharField(max_length=10, blank=False, null=True, default='rating', choices=(
        ('premium', 'premium'),
        ('standard', 'standard'),
        ('deluxe', 'deluxe'),
    ))  
    status = models.CharField(max_length=10, blank=True, null=True, default='num', choices=(
        ('active', 'active'),
        ('num', 'num'),
    ))  
    view1 = models.ImageField(upload_to='media/', blank=False, null=True)
    view2 = models.ImageField(upload_to='media/', blank=False, null=True)
    view3 = models.ImageField(upload_to='media/', blank=False, null=True)
    view4 = models.ImageField(upload_to='media/', blank=False, null=True)
    view5 = models.ImageField(upload_to='media/', blank=False, null=True)
    view6 = models.ImageField(upload_to='media/', blank=True, null=True)
    view7 = models.ImageField(upload_to='media/', blank=True, null=True)
    view8 = models.ImageField(upload_to='media/', blank=True, null=True)
    view9 = models.ImageField(upload_to='media/', blank=True, null=True)
    view10 = models.ImageField(upload_to='media/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message[0:70]