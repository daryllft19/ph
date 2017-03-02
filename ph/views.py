from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.
from models import *
import json


def index(request):
    cluster = Cluster.objects.all()
    context = {'cluster': cluster}
    return render(request, 'app/index.html', context)

def cluster(request, cluster_id):
    location= Location.objects.filter(cluster = cluster_id)
    context = {'location': location}
    return render(request, 'app/cluster.html', context)
