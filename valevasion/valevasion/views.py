from django.shortcuts import render
from travels.models import Info
# Create your views here.

def index(request):
    infos = Info.objects.all().filter(isShow = True)

    return render(request, 'valevasion/home.html', {"infos" : infos})