from rest_framework import serializers
from sendrequest.models import RequestModel
from django.contrib.auth.models import User
from account.models import EmployeeDetailModel

class CheckRequestSerializer(serializers.ModelSerializer):
    remaining_leaves = serializers.SerializerMethodField()
    class Meta:
        model = RequestModel
        fields = ['request_id', 'worker_id', 'created', 'start_date', 'end_date', 'days', 'status', 'remaining_leaves']
        read_only_fields = ['request_id', 'worker_id', 'created', 'start_date', 'end_date', 'days', 'remaining_leaves']

    def get_remaining_leaves(self, obj):
        emp = EmployeeDetailModel.objects.get(worker_id = obj.worker_id)
        return emp.remaining_leaves

class GetWorkerSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'team']
        read_only_fields = ['id', 'username', 'team']

    def get_team(self, obj):
        emp = EmployeeDetailModel.objects.get(worker_id = obj.id)
        return emp.team
