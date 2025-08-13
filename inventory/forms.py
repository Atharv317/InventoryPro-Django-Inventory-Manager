from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    """
    A form to add or edit items in the inventory.
    Automatically maps to the Item model fields.
    """
    class Meta:
        model = Item  # This form is linked to the Item model
        # These are the fields that will appear in the form
        fields = ['name', 'quantity', 'price', 'category', 'low_stock_threshold']
