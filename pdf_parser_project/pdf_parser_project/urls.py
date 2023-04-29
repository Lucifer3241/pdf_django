"""
URL configuration for pdf_parser_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from pdf_parser_app.views import pdf_parser, record_list,download_pdf

app_name = 'pdf_parser'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pdf_parser, name='pdf_parser'),
    path('record_list/', record_list, name='record_list'),
    path('api/',include('pdf_parser_app.urls')),
    path('download_pdf/',download_pdf, name='download_pdf'),
]
