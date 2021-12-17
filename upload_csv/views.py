from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def upload_csv(request):
    return render(request, 'upload_csv.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
