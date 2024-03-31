from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('jobs', views.jobs, name='jobs'),
    path('settings', views.settings, name='settings'),
    path('buy', views.buy, name='buy'),
    path('error', views.error, name='error'),
]
