from django.db import models
from django.conf import settings

class AssetCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(AssetCategory, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
