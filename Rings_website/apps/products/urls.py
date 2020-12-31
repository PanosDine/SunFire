from django.urls import path
from . import views
from .views import JewelView

#path to the page displaying the product
app_name = "products"
urlpatterns = [
    path("", views.JewelView.as_view(), name='products')
]
