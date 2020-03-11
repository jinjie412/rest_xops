"""GrainSupplyCentre URL Configuration

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
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from apps.graincentre.views.login import LoginView
from apps.graincentre.views.out_stock import OutStockView
from apps.graincentre.views.warehous import Warehous
from apps.graincentre.views.warehous_entry import WarehousEntryView
from apps.graincentre.views.warehousout import Warehousout

router = routers.SimpleRouter()
router.register(r'warehous', Warehous, base_name='warehous')
router.register(r'warehousout', Warehousout, base_name='warehousout')

urlpatterns = [
    # re_path(r'login/$', LoginView.as_view()),
    # path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    re_path(r'api/warehousentry/$', WarehousEntryView.as_view()),
    re_path(r'api/warehousentry/(?P<pk>\d+)/$', WarehousEntryView.as_view()),
    re_path(r'outstock/$', OutStockView.as_view()),
]
