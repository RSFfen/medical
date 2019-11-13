from django.urls import path
from . import views
from django.conf.urls import url

from clients.models import Client

#from base.views import ClientAutocomplete # RSF 11/11/2019

urlpatterns = [
    url(r'^$', views.base, name = 'base'), # RSF 13/11/2019    
#    url(r'^$', views.client_autocomplete, name = 'base'), # RSF 12/11/2019    
#    path('client_autocomplete/', views.client_autocomplete, name='client_autocomplete')
    url(r'^clients/$', views.ClientListView.as_view(), name='clients'),
    url(r'^client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    url(r'^firms/$', views.FirmListView.as_view(), name='firms'),
    url(r'^firm/(?P<pk>\d+)$', views.FirmDetailView.as_view(), name='firm-detail'),
    path('client/new/', views.ClientCreateView.as_view(), name='client_new'),
    path('firm/new/', views.FirmCreateView.as_view(), name='firm_new'),
    path('client_autocomplete/', views.client_autocomplete, name='client_autocomplete') # RSF 13/11/2019    
    
]