"""djangoProject URL Configuration

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
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from Archinkluencer.views import Archinkluencer
#from Archinkluencer.views import WallsSel
#from Archinkluencer.views import run
#from  Archinkluencer.views import index
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from . import settings

from django.urls import re_path as url
from Archinkluencer import views



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^archinkluencerhome2/', Archinkluencer),

    #url(r'^archinkluencer01/', WallsSel),
    #path('ArchinkluencerNew2/', views.index, name='index'),
    #path('analyse/', views.run,name='run'),
]

app_name = 'backend'
