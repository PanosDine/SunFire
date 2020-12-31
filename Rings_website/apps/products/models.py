from django.db import models

"""Simple model for the product being sold (jewelry)"""
class Jewel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.title
    
