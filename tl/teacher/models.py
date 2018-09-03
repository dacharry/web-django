from django.db import models

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=50)
    coures = models.CharField(max_length=20)