from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('create/', views.upload_view, name='upload'),
    #path('edit/<str:projectname>', views.edit_model, name='edit_model'),
    path('<str:username>/<str:projectname>', views.open_place_ar, name='place_ar_view'),
]
