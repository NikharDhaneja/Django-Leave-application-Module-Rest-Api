from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import EmployeeDetailModel
from sendrequest.models import RequestModel

# Fill worker_id in EmployeeDetailModel table when new user created
@receiver(post_save, sender = User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if created and not instance.is_superuser:
        e = EmployeeDetailModel(worker_id = instance.id)
        e.save()

# Fill remaining_leaves in EmployeeDetailModel table when leave request is approved by manager
@receiver(post_save, sender = RequestModel)
def request_model_handler(sender, instance, created, *args, **kwargs):
    if instance.status == "Approved":
        e = EmployeeDetailModel.objects.get(worker_id = instance.worker_id)
        e.remaining_leaves = e.remaining_leaves - instance.days
        e.save()
