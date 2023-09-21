from django.db import models

class Booking (models.Model):
    id = models.IntegerField(default=11,primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    bookingdate = models.DateTimeField()
    
class Menu (models.Model):
    id = models.PositiveIntegerField(default=5,primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.PositiveIntegerField(default=5)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'