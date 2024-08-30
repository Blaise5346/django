from django.contrib import admin

# Register your models here.

from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_description', 'entry_date', 'taken_date', 'item_came_from', 'quantity')
    list_filter = ('entry_date', 'taken_date', 'item_came_from')
    search_fields =('item_name', 'item_description')