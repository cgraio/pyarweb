# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from .views import (
    irc,
    quienes_somos,
    MiembrosDePyAr,
    ListaDeCorreo
)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('community.urls')),
    url(r'^irc/', irc),
    url(r'^quienes_somos/', quienes_somos),
    url(r'^MiembrosDePyAr/', MiembrosDePyAr),
    url(r'^ListaDeCorreo/', ListaDeCorreo),
    url(r'^news', include('news.urls')),
    url(r'^companies', include('pycompanies.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pyarenses/', include('registration.backends.default.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
