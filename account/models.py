from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetailModel(models.Model):
    worker = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    team = models.CharField(max_length=12, blank = True)
    remaining_leaves = models.IntegerField(default = 30)
