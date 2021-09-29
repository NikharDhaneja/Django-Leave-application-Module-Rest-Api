from rest_framework.views import APIView
from .serializers import CheckRequestSerializer,GetWorkerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager
from sendrequest.models import RequestModel
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,authentication_classes,permission_classes
# Create your views here.
class CheckRequestView(APIView):

    authentication_classes = [ JWTAuthentication ]
    permission_classes = [IsAuthenticated, IsManager]
    serializer_class = CheckRequestSerializer

    def get(self, request, format=None):
        requests = RequestModel.objects.filter(manager_id = request.user.id, status = "Pending").order_by("created")
        serializer = CheckRequestSerializer(requests, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        modelinstance = RequestModel.objects.get(request_id = pk)
        serializer = CheckRequestSerializer(modelinstance, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsManager])
def get_worker_profile(request, pk, format=None):
    worker = User.objects.get(id = pk)
    serializer = GetWorkerSerializer(worker)
    return Response(serializer.data)
