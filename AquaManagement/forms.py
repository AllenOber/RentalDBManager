from django import forms
from .models import WorkOrder, RentalOrder, BCD  # Imported my models


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'  # all fields


class RentalOrderForm(forms.ModelForm):
    class Meta:
        model = RentalOrder
        fields = '__all__'  # all fields


class BCDEquipmentForm(forms.ModelForm):
    class Meta:
        model = BCD
        fields = '__all__'  # all fields
