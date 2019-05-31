"""onionsv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import api_reader

urlpatterns = [
    url(r'^$', api_reader.blank , name='blank'),
    url(r'^dbping/', api_reader.dbping, name='dbping'),
    url(r'^createtb$', api_reader.createtb, name='createtb'),
    url(r'^showtable$', api_reader.showtable, name='showtable'),
    url(r'^addManyPoints$', api_reader.addManyPoints, name='addManyPoints'),
]

