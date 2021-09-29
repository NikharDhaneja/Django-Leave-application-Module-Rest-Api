from django.urls import path
from .views import CheckRequestView
from .views import get_worker_profile

urlpatterns = [
    path('checkrequest/api/', CheckRequestView.as_view(), name='get_request_view'),
    path('checkrequest/api/<int:pk>/', CheckRequestView.as_view(), name='patch_request_view'),
    path('checkrequest/api/workerid/<int:pk>/', get_worker_profile, name='get_worker_view'),
]
