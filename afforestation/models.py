from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Planted_trees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Project_Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Date_of_Plantation = models.DateField()
    Species_Planted = models.CharField(max_length=100)
    Area_Planted = models.IntegerField()
    Number_of_Trees_Planted=models.IntegerField()
    Planting_Density=models.IntegerField()
    Action=models.CharField(max_length=100)

class Trees_Species(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Species_Planted = models.CharField(max_length=100)
    Growth_Rate_Height = models.FloatField()
    Growth_Rate_Diameter = models.IntegerField()
    Survival_Rate = models.IntegerField()
    Above_Ground_Biomass = models.IntegerField()
    Below_Ground_Biomass = models.IntegerField()
    Action=models.CharField(max_length=100)
