from django.db import models

# Create your models here.

class job(models.Model):
    type =models.CharField(max_length=255)
    salary=models.IntegerField(max_length=10)
    Exp=models.CharField(max_length=255)
    Requirnments=models.CharField(max_length=255)
    

def __str__(self):
    return self.title


