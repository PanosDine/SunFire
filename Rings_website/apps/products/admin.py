from django.contrib import admin
from .models import Jewel

"""class that displays the Jewel model in a tabular form so the admin can edit,
add and delete a Jewel object from their interface"""

"""How to choose the order of fields"""
class JewelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'price', 'image']}),
    ]
    list_display = ('title', 'description', 'price', 'image')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Jewel, JewelAdmin)
