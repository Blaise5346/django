from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'entry_date', 'taken_date', 'item_came_from', 'quantity')