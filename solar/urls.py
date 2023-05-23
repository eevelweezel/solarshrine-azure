"""solar URL Configuration

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
import captcha.urls
import ckeditor_uploader.urls
from django.conf import settings
from django.contrib import admin
from django.urls import (
    include,
    path,
    re_path
)
from django.conf.urls.static import static

from solar import views

urlpatterns = [
    path('', views.get_home_page),
    path('pages/<slug:slug>/', views.get_post, name="show_post"),
    path('admin/', admin.site.urls),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('thanks/', views.thanks_view, name="thanks"),
    re_path(r'^ckeditor/', include(ckeditor_uploader.urls)),
    re_path(r'^captcha/', include(captcha.urls)),
]
if settings.DEBUG:
     urlpatterns += \
         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += \
         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
