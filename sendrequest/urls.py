from django.urls import path
from .views import SendRequestView

app_name = 'sendrequest'
urlpatterns = [
    path('sendrequest/api/', SendRequestView.as_view(), name='send_request_view'),
]
