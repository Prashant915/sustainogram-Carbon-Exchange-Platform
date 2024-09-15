from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class resource(models.Model):
    Image=models.ImageField(upload_to="Resource",blank=False,null=False,default=None,)
    Title=models.CharField(max_length=40,blank=False,null=False,)
    Description=HTMLField(max_length=4000,blank=False,null=False,)
    Highlight=models.CharField(max_length=350,blank=False,null=False,)
    
