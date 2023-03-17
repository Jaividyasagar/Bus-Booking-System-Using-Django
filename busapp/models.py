from django.db import models
from datetime import time
# Create your models here.
class BusDetails(models.Model):
    bus_no = models.IntegerField()
    departure_time = models.TimeField(default=time)
    dest = (('Villupuram','Villupuram'),('Chengalpattu','Chengalpattu'),('Chennai','Chennai'),)
    # dest = ((0,'Villupuram'),(1,'Chengalpattu'),(2,'Chennai'),)
    destinations = models.TextField(choices=dest,default='Chennai')
    seats_available = models.IntegerField()
    tc = ((100,100),(150,150),(200,200),)
    ticket_costs = models.IntegerField(choices=tc,default=200)

    def __str__(self):
        return "Bus Number: " + str(self.bus_no)
