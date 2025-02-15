"""PhySim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from PhySim.views import hello_world, root_page, text_render

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello_world/$', hello_world),
    url(r'^$', root_page),
    url(r'^whatever/$', TemplateView.as_view(template_name = "PhySim/SampleHTML.html"), name = 'whatever'),

]
