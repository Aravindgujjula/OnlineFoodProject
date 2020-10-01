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

from vendor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.openlogin,name = "vendor_main"),
    path('vendor_login_check/',views.vendor_login_check,name = "vendor_login_check"),
    path('vendor_register/',views.vendor_register,name='vendor_register'),
    path('vendor_save/',views.vendor_save,name="vendor_save"),
    path('vendor_welcome/<int:pk>/',views.vendor_welcome,name = "vendor_welcome"),
    path('vendor_logout/',views.vendor_login_check,name="vendor_logout"),
    path('Vendor_foodtype/',views.Vendor_foodtype,name="Vendor_foodtype"),
    path('vendor_save_foodtype/',views.vendor_save_foodtype,name="vendor_save_foodtype"),
    path('Vendor_food/',views.Vendor_food,name="Vendor_food"),
    path('vendor_save_food/',views.vendor_save_food,name="vendor_save_food"),
    path('vendor_customer_order/',views.vendor_customer_order,name="vendor_customer_order"),
]
