from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Rooms(TemplateView):
    template_name = "rooms.html"
