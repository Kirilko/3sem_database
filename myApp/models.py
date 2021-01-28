from django.db import models


# Create your models here.
class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Drug_Description(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    group = models.ForeignKey(Group, related_name="drug_description_group", on_delete=models.CASCADE)
    description = models.CharField(max_length=40, null=True)


class Indication(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Drug_Description_Indication(models.Model):
    drug_description = models.ForeignKey(Drug_Description, related_name="drug_description1", on_delete=models.CASCADE)
    indication = models.ForeignKey(Indication, related_name="indication_name", on_delete=models.CASCADE)


class Contraindication(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Drug_Description_Contraindication(models.Model):
    drug_description = models.ForeignKey(Drug_Description, related_name="drug_description2", on_delete=models.CASCADE)
    indication = models.ForeignKey(Contraindication, related_name="contraindication_name", on_delete=models.CASCADE)


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Manufacturer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, related_name="country_name", on_delete=models.CASCADE)
    description = models.CharField(max_length=40, null=True)


class Type(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Drug(models.Model):
    id = models.IntegerField(primary_key=True)
    drug_description = models.ForeignKey(Drug_Description, related_name="drug_description3", on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name="type_id", on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, related_name="manufacturer_id", on_delete=models.CASCADE)
    shelf_life = models.DateField()


class Specialization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Drug_Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    specialization = models.ForeignKey(Specialization, related_name="specialization_id", on_delete=models.CASCADE)
    description = models.CharField(max_length=40, null=True)


class Drug_Drug_Store(models.Model):
    drug = models.ForeignKey(Drug, related_name="drug_id", on_delete=models.CASCADE)
    drug_store = models.ForeignKey(Drug_Store, related_name="drug_store_id", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
