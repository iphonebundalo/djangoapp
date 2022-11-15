from django.db import models
from django.contrib.gis.db import models

class stub(models.Model):
    tip_stuba = models.CharField(max_length=100)
    lokacija = models.PointField()
    adresa = models.CharField(max_length=100)
    grad = models.CharField(max_length=50)
    konzola = models.CharField(max_length=100)
    izolator = models.CharField(max_length=100)
    provodnik = models.CharField(max_length=100)
    
    


# Create your models here.
