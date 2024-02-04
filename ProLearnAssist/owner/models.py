from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class teach_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    message=models.CharField(max_length=255)
    request_status=models.BooleanField(default=True)
