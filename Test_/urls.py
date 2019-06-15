"""Test_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import include, path
from .settings import *
import xadmin
xadmin.autodiscover()

#version模块自动注册需要版本控制的model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url('^xadmin/', xadmin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'', include(('Django_web.urls', 'Django_web'), namespace= 'Django_web')),
]



if DEBUG:
    media_root = os.path.join(BASE_DIR, MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

