from rest_framework.views import APIView
from .models import RequestModel
from .serializers import SendRequestGetSerializer, SendRequestPostSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import datetime
from account.models import EmployeeDetailModel
from rest_framework.renderers import TemplateHTMLRenderer

class SendRequestView(APIView):

    authentication_classes = [ JWTAuthentication ]
    permission_classes = [IsAuthenticated]
    # serializer_class = SendRequestSerializer

    def get(self, request, format=None):
        requests = RequestModel.objects.filter(worker_id = request.user.id).order_by("-created")
        serializer = SendRequestGetSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        emp = EmployeeDetailModel.objects.get(worker = request.user.id)
        manager = User.objects.get(is_staff = True, employeedetailmodel__team = emp.team)

        context = {"worker_id": request.user.id}
        serializer = SendRequestPostSerializer(data=request.data, context=context)
        if serializer.is_valid():
            data = dict(worker_id = request.user.id,
                        manager_id = manager.id,
                        start_date = serializer.validated_data['start_date'],
                        end_date = serializer.validated_data['end_date'],
                        days = serializer.validated_data['days'])
            modelinstance = RequestModel.objects.create(**data)
            modelinstance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
