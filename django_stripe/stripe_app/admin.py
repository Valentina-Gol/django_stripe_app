from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    search_fields = ('name', "price")


admin.site.register(Item, ItemAdmin)
