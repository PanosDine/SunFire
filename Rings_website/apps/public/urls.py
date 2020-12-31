from django.urls import path

from . import views

"""the 'public' app holds together the pages that don't need any models
or complicated views, like the 'index' and 'about'"""

app_name="public"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]
