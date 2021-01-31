"""distribuidoraHawaii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from distribuidoraHawaii import settings
from django.urls import re_path
from django.views.static import serve

from webApp.views import home_view, contact_view, about_view, productos_view, blog_view

urlpatterns = [
    path('',home_view, name='home'),
    path('contacto/',contact_view, name='contact'),
    path('acercade/',about_view, name='acerca'),
    path('productos/',productos_view, name='productos'),
    path('blog/',blog_view, name='blog'),
    path('admin/', admin.site.urls),
    
]


urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
           'document_root': settings.STATIC_ROOT,
        }),
    ]
