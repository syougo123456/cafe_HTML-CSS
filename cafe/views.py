from re import A
from django.shortcuts import render
from django.views.generic import ListView
from .models import Cafe

class CafeList(ListView):
    template_name = 'cafe/index.html'
    model = Cafe