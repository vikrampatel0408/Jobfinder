from django.db import models

# Create your models here.
class company(models.Model):
    comp_name =models.CharField(max_length=255)
    comp_email=models.CharField(max_length=255)
    ID=models.CharField(max_length=255)
    Telephone_no=models.IntegerField(max_length=10)
    estd_year=models.DateField()
    location=models.CharField(max_length=255)

def __str__(self):
    return self.title
