"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from liblab import views as liblab_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', liblab_views.index , name='index'),
    url(r'^index/', liblab_views.index, name='index'),
    url(r'^books/', liblab_views.books, name='books'),
    url(r'^dvds/', liblab_views.dvds, name='dvds'),
    url(r'^others/', liblab_views.others, name='others'),
    url(r'^about/', liblab_views.about, name='about'),
    url(r'^myacct/', liblab_views.myacct, name='myacct'),
    url(r'^register/', liblab_views.register, name='register'),
    url(r'^base/', liblab_views.base, name='base'),
]
