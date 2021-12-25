"""dictionaryWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from lang_lang.views import home_view, language_detail_view, language_api_detail_view

urlpatterns = [
    path('languages/<int:id>/', language_detail_view),
    path('api/languages/<int:id>/', language_api_detail_view),
    path('home/', home_view),
    path('admin/', admin.site.urls),
]
