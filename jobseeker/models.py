from django.db import models

# Create your models here.
class jobseeker(models.Model):
    name =models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    
def __str__(self):
    return self.title

