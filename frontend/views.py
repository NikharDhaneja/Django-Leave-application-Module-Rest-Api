from django.shortcuts import render, redirect



# Create your views here.
def loginView(request):
    return render(request, 'login.html')

def sendrequestView(request):
        return render(request, 'sendrequest.html')

def checkrequestView(request):
    return render(request, 'checkrequest.html')
