from django.db import models
from django.contrib.auth.models import User

class user_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    Phone=models.BigIntegerField(null=True)
    Qualification=models.CharField(max_length=100,null=False)
    Interest=models.CharField(max_length=100,null=False)
    CurrentStatus=models.CharField(max_length=100,null=True)
    Institution=models.CharField(max_length=100,null=False)
    # Country=models.CharField(max_length=100,null=True)
    # City=models.CharField(max_length=100,null=True)
    # Landmark=models.CharField(max_length=100,null=True)
    # DOB=models.CharField(max_length=100,null=True)
    
