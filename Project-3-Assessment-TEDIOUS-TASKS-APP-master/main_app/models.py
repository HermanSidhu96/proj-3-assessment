from django.db import models

# Create your models here.



class Task(models.Model):
    description  = models.CharField(max_length=200)
    time  = models.IntegerField()
    person  = models.CharField(max_length=200)
    # name = models.CharField(max_length=200)