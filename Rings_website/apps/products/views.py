from django.shortcuts import render
from .models import Jewel
from django.views import generic

#a view for the jewel model
class JewelView(generic.ListView):
    model = Jewel
    context_object_name = 'jewel_list'
    template_name = '../templates/products.html'
