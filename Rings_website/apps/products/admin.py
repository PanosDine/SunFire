from django.contrib import admin
from .models import Jewel

"""class RingInline(admin.TabularInline):
    model = Ring
    extra = 3"""

"""How to choose the order of fields"""
class JewelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'description', 'price', 'image']}),
    ]
    #inlines = [RingInline]
    list_display = ('title', 'description', 'price', 'image')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Jewel, JewelAdmin)
