from django.contrib import admin


# Register your models here.
from myApp.models import Group, Drug_Description, Indication, Drug_Description_Indication, Contraindication, \
    Drug_Description_Contraindication, Country, Manufacturer, Type, Drug, Specialization, Drug_Store, Drug_Drug_Store

admin.site.register(Group)
admin.site.register(Drug_Description)
admin.site.register(Indication)
admin.site.register(Drug_Description_Indication)
admin.site.register(Contraindication)
admin.site.register(Drug_Description_Contraindication)
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Type)
admin.site.register(Drug)
admin.site.register(Specialization)
admin.site.register(Drug_Store)
admin.site.register(Drug_Drug_Store)


