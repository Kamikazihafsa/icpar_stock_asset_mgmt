from django import forms
from .models import Asset, AssetCategory

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetCategoryForm(forms.ModelForm):
    class Meta:
        model = AssetCategory
        fields = '__all__'
