from rest_framework.serializers import ModelSerializer
from myApp.models import Group, Drug_Description, Indication, Drug_Description_Indication, Contraindication, \
    Drug_Description_Contraindication, Country, Manufacturer, Type, Drug, Specialization, Drug_Store, Drug_Drug_Store


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class Drug_DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Drug_Description
        fields = ['id', 'name', 'group', 'description']


class IndicationSerializer(ModelSerializer):
    class Meta:
        model = Indication
        fields = ['id', 'name']


class Drug_Description_IndicationSerializer(ModelSerializer):
    class Meta:
        model = Drug_Description_Indication
        fields = ['drug_description', 'indication']


class ContraindicationSerializer(ModelSerializer):
    class Meta:
        model = Contraindication
        fields = ['id', 'name']


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'description']


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class DrugSerializer(ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'drug_description', 'type', 'manufacturer', 'shelf_life']


class SpecializationSerializer(ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name']


class Drug_Description_ContraindicationSerializer(ModelSerializer):
    class Meta:
        model = Drug_Description_Contraindication
        fields = ['drug_description', 'indication']


class Drug_StoreSerializer(ModelSerializer):
    class Meta:
        model = Drug_Store
        fields = ['id', 'name', 'address', 'district', 'phone','specialization','description']


class Drug_Drug_StoreSerializer(ModelSerializer):
    class Meta:
        model = Drug_Drug_Store
        fields = ['drug', 'drug_store', 'quantity', 'price']
