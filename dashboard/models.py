from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class User_Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    country=models.CharField(max_length=50,default=None)
    mobile=models.CharField(max_length=12)
    company=models.CharField(max_length=50,default=None)

project_type={
    "A/R":"A/R",
    "Biogas - Cogeneration":"Biogas - Cogeneration",
    "Biogas - Electricity":"Biogas - Electricity",
    "Biogas - Heat":"Biogas - Heat",
    "Biogas - Transportation":"Biogas - Transportation",
    "Biomass, or Liquid Biofuel - Cogeneration":"Biomass, or Liquid Biofuel - Cogeneration",
    "Biomass, or Liquid Biofuel - Electricity":"Biomass, or Liquid Biofuel - Electricity",
    "Biomass, or Liquid Biofuel - Heat":"Biomass, or Liquid Biofuel - Heat",
    "CSA":"CSA",
    "Clean Water Access":"Clean Water Access",
    "Energy Efficiency - Agriculture Sector":"Energy Efficiency - Agriculture Sector",
    "Energy Efficiency - Commercial Sector":"Energy Efficiency - Commercial Sector",
    "Energy Efficiency - Domestic":"Energy Efficiency - Domestic",
    "Energy Efficiency - Industrial":"Energy Efficiency - Industrial",
    "Energy Efficiency - Public Sector":"Energy Efficiency - Public Sector",
    "Energy Efficiency - Transport Sector":"Energy Efficiency - Transport Sector",
    "Geothermal":"Geothermal",
    "Liquid Biofuel - Transportation":"Liquid Biofuel - Transportation",
    "Other":"Other",
    "PV":"PV",
    "Small, Low - Impact Hydro":"Small, Low - Impact Hydro",
    "Solar Thermal - Electricity":"Solar Thermal - Electricity",
    "Solar Thermal - Heat":"Solar Thermal - Heat",
    "WASH":"WASH",
    "Wind":"Wind"
}

product_type={
    "VER":"VER",
    "PER":"PER",
    "CER":"CER"
}

status={
    "Retired":"Retired",
    "Assigned":"Assigned"
}

class Issuence(models.Model):
    Vintage = models.IntegerField(default=datetime.now().year)
    Quantity = models.IntegerField()
    S_ID = models.CharField(max_length=10, unique=True, blank=False, editable=False)
    Project_Name = models.CharField(max_length=100,default=None)
    Developed_BY= models.CharField(max_length=100)
    POA_S_ID = models.CharField(max_length=15, unique=True, blank=False, editable=False)
    Project_Type = models.CharField(max_length=60, choices=project_type)
    Product_type = models.CharField(max_length=5, choices=product_type)
    Issuence_Date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.S_ID:
            last_product = Issuence.objects.all().order_by('id').last()
            if last_product and last_product.S_ID:
                last_id = last_product.S_ID
                new_id = int(last_id[1:]) + 1
                self.S_ID = f'S{new_id:03d}'
            else:
                self.S_ID = 'S001'
        
        if not self.POA_S_ID:
            last_product = Issuence.objects.all().order_by('id').last()
            if last_product and last_product.POA_S_ID:
                last_id = last_product.POA_S_ID
                new_id = int(last_id.split('_')[-1]) + 1
                self.POA_S_ID = f'POA_S_{new_id:03d}'
            else:
                self.POA_S_ID = 'POA_S_001'

        super(Issuence, self).save(*args, **kwargs)

# class retirement(models.Model):
#     Vintage = models.IntegerField(choices=year)
#     Status = models.CharField(max_length=10,choices=status)
#     Quantity = models.IntegerField()