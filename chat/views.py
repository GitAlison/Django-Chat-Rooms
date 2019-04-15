from django.shortcuts import render
from django.views.generic import TemplateView,View,DetailView
from django.views.generic.edit import CreateView
# Create your views here.
from .models import Room

class Rooms(View):
    template_name = "rooms.html"
    def get(self,request):
        rooms = Room.objects.all()
        contexto = {
            'rooms': rooms
        }
        return render(request,self.template_name,contexto)


class RoomDetail(DetailView):
    template_name = "rooms.html"
    model = Room

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context
