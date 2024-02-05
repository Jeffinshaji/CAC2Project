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

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    name=models.CharField(max_length=100,null=True)
    Date=models.DateField(null=False)
    Instructor=models.CharField(max_length=100,null=False)
    Content=models.IntegerField(null=False)
    levelofteaching=models.IntegerField(null=False)
    Material=models.IntegerField(null=False)
    Rating=models.IntegerField(null=False)
    Overallrating=models.IntegerField(null=False)
    Comments=models.CharField(max_length=100,null=False) 
    
class interests(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=0)
    Subject=models.CharField(max_length=100,null=False)
    Teaching_status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Subject.__str__())
    
class improvements(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=0)
    Subject=models.CharField(max_length=100,null=False)
    Learning=models.CharField(max_length=100,null=False,default="No")

    def __str__(self):
        return str(self.Subject.__str__())