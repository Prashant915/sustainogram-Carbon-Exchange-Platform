from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ApiData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehicle_Model_No = models.CharField(max_length=100)
    Type_of_Material = models.CharField(max_length=100)
    Supplier_Name = models.CharField(max_length=100)
    Weight_of_Material = models.FloatField()
    Percentage_Composition = models.FloatField()

class evusage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehicle_Model_No = models.CharField(max_length=100)
    Vehicle_ID = models.CharField(max_length=100)
    Owner_Name = models.CharField(max_length=100)
    Sold_Date = models.DateField()
    Daily_Operational_KM = models.IntegerField()
    Total_KM_Operation = models.IntegerField()
    Source_of_Power = models.CharField(max_length=40)