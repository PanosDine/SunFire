from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

"""simple views, no real functionality here, just rendering the 
corresponding templates"""
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')
