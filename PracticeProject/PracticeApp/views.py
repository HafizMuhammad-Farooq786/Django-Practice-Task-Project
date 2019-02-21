from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request):
    today = datetime.now().date()
    return render(request, 'index.html', {'today': today})

