from django.db import models

# Create your models here.


class donations(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ETH = models.DecimalField(max_digits=100, decimal_places=30)
    note = models.CharField(max_length=500)
