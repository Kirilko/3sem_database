"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import SimpleRouter

from myApp.views import initial_page, GroupView, initial_app, IndicationView, ContraindicationView, \
    Drug_DescriptionView, Drug_Description_IndicationView, Drug_Description_ContraindicationView, CountryView, \
    ManufacturerView, TypeView, DrugView, SpecializationView, Drug_StoreView, Drug_Drug_StoreView

router = SimpleRouter()

router.register('api/group', GroupView)
router.register('api/indication', IndicationView)
router.register('api/contraindication', ContraindicationView)
router.register('api/dd', Drug_DescriptionView)
router.register('api/ddi', Drug_Description_IndicationView)
router.register('api/ddc', Drug_Description_ContraindicationView)
router.register('api/country', CountryView)
router.register('api/manufacturer', ManufacturerView)
router.register('api/type', TypeView)
router.register('api/drug', DrugView)
router.register('api/specialization', SpecializationView)
router.register('api/drugstore', Drug_StoreView)
router.register('api/dds', Drug_Drug_StoreView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initial_app),
    path('orders_page/', initial_app),
]

urlpatterns += router.urls
