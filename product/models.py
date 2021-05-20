from django.db import models

class Product(models.Model):
    header = models.CharField("header", max_length=240)
    subheader = models.CharField(max_length=240)
    leftheader = models.CharField(max_length=240)
    leftsubheader = models.CharField(max_length=240)
    rightheader = models.CharField(max_length=240)
    rightsubheader = models.CharField(max_length=240)

    def __str__(self):
        return self.header
# Create your models here.
