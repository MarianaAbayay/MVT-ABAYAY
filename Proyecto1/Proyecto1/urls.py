"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.AppFlia.views import familiar1
from Proyecto1.views import inicio, familiares 
from AppFlia.views import familiar1, familiar2, familiar3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name=inicio),
    path('familiares/', familiares, name="familiares"),
    path('primerfamiliar/', familiar1, name="familiar1"),
    path('segundofamiliar/', familiar2, name="familiar2"),
    path('tercerfamiliar/',familiar3, name="familiar3"),
]
