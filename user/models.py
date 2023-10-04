from django.db import models

class CarListing(models.Model):
    company = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    looking_for = models.TextField()  
    specifications = models.TextField()  
    car_type = models.TextField()  
    ppc_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)     


    def __str__(self):
        return self.company