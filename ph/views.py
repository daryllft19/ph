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

def canvas(request):
    cluster = Cluster.objects.all()
    context = {'cluster': cluster}
    return render(request, 'canvas/index.html', context)

def canvas_package(request, cluster_id):
    locations = Location.objects.filter(cluster=cluster_id)
    package= Package.objects.filter(location_id__in=[x.id for x in locations])
    context = {'package': package}
    return render(request, 'canvas/package.html', context)
