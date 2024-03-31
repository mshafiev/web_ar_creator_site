from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import Register, EmailVerify, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register', Register.as_view(template_name='registration/register.html'), name='register'),
    path('verify_email/<str:uid64>/<str:token>/', EmailVerify.as_view(), name="verify_email"),
    path('invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email')
]
