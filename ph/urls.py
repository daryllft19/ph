from django.conf.urls import url
import views, api

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^cluster/(?P<cluster_id>[0-9]+)/$', views.cluster, name='cluster'),


    url(r'^api/cluster/(?P<cluster_id>[0-9]+)/$', api.cluster, name='cluster'),
    url(r'^api/location/(?P<location_id>[0-9]+)/$', api.location, name='location'),
    url(r'^api/package/(?P<package_id>[0-9]+)/$', api.package, name='package'),
    url(r'^api/cluster/(?P<cluster_id>[0-9]+)/location$', api.cluster_location, name='cluster_location'),
    url(r'^api/location/(?P<location_id>[0-9]+)/package$', api.location_package, name='location_package')
]