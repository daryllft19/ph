from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from models import *
import json


def cluster(request, cluster_id):
    obj = Cluster.objects.get(pk = cluster_id)
    return  JsonResponse(obj.to_dict())

def location(request, location_id):
    # obj = model_to_dict(Location.objects.get(pk = location_id))
    obj = Location.objects.get(pk = location_id)
    return  JsonResponse(obj.to_dict())

def package(request, package_id):
    obj = Package.objects.get(pk = package_id)
    return  JsonResponse(obj.to_dict())

def cluster_location(request, cluster_id):
    obj = Location.objects.filter(cluster = cluster_id)
    out = {}
    for i, o in enumerate(obj):
        out[i] = o.to_dict()

    return  JsonResponse(out)

def location_package(request, location_id):
    obj = Package.objects.filter(location=location_id)
    out = {}
    for i, o in enumerate(obj):
        out[i] = o.to_dict()

    return JsonResponse(out)
