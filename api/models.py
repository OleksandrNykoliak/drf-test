from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.name

class RealEstate(models.Model):
    # (квартира, земля, будинок)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(
        'Manager', on_delete=models.CASCADE, related_name='real_estates')
    owner = models.ForeignKey(
        'Seller', on_delete=models.CASCADE, related_name='real_estates')
    
    
    def __str__(self):
        return self.name


class RealEstateDetails(models.Model):
    real_estate = models.OneToOneField(
        'RealEstate', on_delete=models.CASCADE, related_name='details')
    square = models.FloatField(default=None)
    number_of_rooms = models.IntegerField(default=None)
    floor = models.IntegerField(default=None)
    number_of_floors = models.IntegerField(default=None)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default=None)
    price_per_month = models.FloatField(default=None, null=True, blank=True)
    price_per_day = models.FloatField(default=None, null=True, blank=True)
    price_per_year = models.FloatField(default=None, null=True, blank=True)
    
    
    def __str__(self):
        return self.real_estate.name
