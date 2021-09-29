from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class RequestModel(models.Model):
    # g_start_date = 0
    # def validate_start_date(value):
    #     if value < date.today():
    #         raise ValidationError("You only take date from tomorrow")
    #     else:
    #         RequestModel.g_start_date = value
    #         return value
    #
    # def validate_end_date(value):
    #     if value < RequestModel.g_start_date:
    #         raise ValidationError("End date must be come after start_date")
    #     else:
    #         return value

    STATUS_CHECK = (
                    ("Pending","Pending"),
                    ("Approved","Approved"),
                    ("Rejected","Rejected")
                    )
    request_id = models.AutoField(primary_key = True)
    worker_id = models.IntegerField()
    manager_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    # start_date = models.DateField(validators = [validate_start_date])
    # end_date = models.DateField(validators = [validate_end_date])
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.IntegerField()
    status = models.CharField(max_length=8, choices = STATUS_CHECK, default='Pending')
