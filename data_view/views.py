from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def view(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        data = pd.read_csv(request.FILES['csv_file'], sep=',')
        print(data)
    return HttpResponse(data['etage'][30])
