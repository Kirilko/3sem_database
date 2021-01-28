from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from myApp.models import Group, Drug_Description, Indication, Drug_Description_Indication, Contraindication, \
    Drug_Description_Contraindication, Country, Manufacturer, Type, Drug, Specialization, Drug_Store, Drug_Drug_Store
from myApp.serializer import GroupSerializer, Drug_DescriptionSerializer, IndicationSerializer, \
    Drug_Description_IndicationSerializer, ContraindicationSerializer, Drug_Description_ContraindicationSerializer, \
    CountrySerializer, ManufacturerSerializer, TypeSerializer, DrugSerializer, SpecializationSerializer, \
    Drug_StoreSerializer, Drug_Drug_StoreSerializer


def initial_page(request):
    return render(request, 'index.html',
                  {'group': Group.objects.all(),
                   'drug_description': Drug_Description.objects.all(),
                   'indications': Indication.objects.all(),
                   "drug_description_indication": Drug_Description_Indication.objects.all(),
                   "contraindication": Contraindication.objects.all(),
                   "drug_description_contraindication": Drug_Description_Contraindication.objects.all(),
                   "country": Country.objects.all(), 'manufacturer': Manufacturer.objects.all(),
                   'type': Type.objects.all(),
                   'drug': Drug.objects.all(), 'specialization': Specialization.objects.all(),
                   'drug_store': Drug_Store.objects.all(),
                   'drug_drug_store': Drug_Drug_Store.objects.all()})


def initial_app(request):
    return render(request, 'main_app.html')


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Drug_DescriptionView(ModelViewSet):
    queryset = Drug_Description.objects.all()
    serializer_class = Drug_DescriptionSerializer


class IndicationView(ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer


class Drug_Description_IndicationView(ModelViewSet):
    queryset = Drug_Description_Indication.objects.all()
    serializer_class = Drug_Description_IndicationSerializer


class ContraindicationView(ModelViewSet):
    queryset = Contraindication.objects.all()
    serializer_class = ContraindicationSerializer


class Drug_Description_ContraindicationView(ModelViewSet):
    queryset = Drug_Description_Contraindication.objects.all()
    serializer_class = Drug_Description_ContraindicationSerializer


class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ManufacturerView(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class TypeView(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class DrugView(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class SpecializationView(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class Drug_StoreView(ModelViewSet):
    queryset = Drug_Store.objects.all()
    serializer_class = Drug_StoreSerializer


class Drug_Drug_StoreView(ModelViewSet):
    queryset = Drug_Drug_Store.objects.all()
    serializer_class = Drug_Drug_StoreSerializer
