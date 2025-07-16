from django import forms
from .models import StockItem, StockMovement

class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = '__all__'

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = '__all__'
