from django.urls import path, include
from . import views
from Register import views as v
from Register.views import ProfileUpdateView
app_name = 'main'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("register/", v.register, name = 'register'),
]