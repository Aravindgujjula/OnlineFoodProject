"""OnlineFood URL Configuration

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
from pwn import views

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('',views.showIndex,name = "pwn_main"),
    path('pwn_login_check/',views.pwn_login_check,name = "pwn_login_check"),
    path('welcome/',views.welcome,name = "welcome"),

    path('state/',views.openstate,name = "state"),
    path('savestate/',views.savestate,name='savestate'),
    path('updatestate/',views.updatestate,name='updatestate'),
    path('updatestateid/',views.updatestateid,name='updatestateid'),
    path('sdelete/',views.sdelete,name='sdelete'),

    path('city/',views.opencity,name = "city"),
    path('savecity/',views.savecity,name='savecity'),

    path('cusine/',views.opencusine,name = "cusine"),
    path('savecusine/',views.savecusine,name = "savecusine"),

    path('vendor/',views.openvendor,name = "vendor"),
    path('pwn_vendor_approve/',views.pwn_vendor_approve,name = "pwn_vendor_approve"),
    path('pwn_vendor_cancel/',views.pwn_vendor_cancel,name="pwn_vendor_cancel"),

    path('reports/', views.openreports, name="reports"),

    path('logout/',views.pwn_login_check,name = "logout"),

]
