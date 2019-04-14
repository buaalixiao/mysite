"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import mysite.views as mysite_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^hello/$', mysite_view.hello),
	url(r'^time/$', mysite_view.current_time),
	url(r'^time/plus/(\d{1,2})/$', mysite_view.hours_ahead),
	url(r'^$', mysite_view.index),
    url(r'^test/(?P<page>\S+)/$', mysite_view.test),
]
