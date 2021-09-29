from rest_framework import serializers
from .models import RequestModel
from account.models import EmployeeDetailModel
from datetime import date
from datetime import datetime

class SendRequestGetSerializer(serializers.ModelSerializer):
    remaining_leaves = serializers.SerializerMethodField()
    class Meta:
        model = RequestModel
        fields = ['request_id', 'start_date', 'end_date', 'status', 'remaining_leaves']
        read_only_fields = ['request_id', 'status', 'remaining_leaves']

    def get_remaining_leaves(self, obj):
        emp = EmployeeDetailModel.objects.get(worker_id = obj.worker_id)
        return emp.remaining_leaves


class SendRequestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = ['start_date', 'end_date']

    def validate(self, data):
        format_str = '%Y-%m-%d'
        # delta = datetime.strptime(data['end_date'], format_str) - datetime.strptime(data['start_date'], format_str)
        delta = data['end_date'] - data['start_date']
        days = delta.days
        data["days"] = days

        id = self.context.get("worker_id")
        emp = EmployeeDetailModel.objects.get(worker_id = id)
        remaining_leaves= emp.remaining_leaves

        if (data['start_date'] <= date.today()):
            raise serializers.ValidationError({"error": "start_date must occur after today"}) # raises when start_date after today.

        elif (data['start_date'] >= data['end_date']):
                raise serializers.ValidationError({"error": "end_date must occur after start_date"}) # raises when start_date is before the end_date.

        elif(days > remaining_leaves):
            raise serializers.ValidationError({"error": "you have only"+str(remaining_leaves)+" leaves"}) # raises when asking leave is more than remaining_leaves.

        return data
