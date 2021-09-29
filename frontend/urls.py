from django.urls import path
from .views import loginView, sendrequestView, checkrequestView

# app_name = 'frontend'
urlpatterns = [
    path('', loginView, name='login_view'),
    path('sendrequest/', sendrequestView, name='sendrequest_view'),
    path('checkrequest/', checkrequestView, name='checkrequest_view'),
]
