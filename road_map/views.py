from django.shortcuts import render
from django.http import response
from .models import MainQuest, MainBlock, Events
# Create your views here.


def first(request):
    event_context = {}
    event_context["main_quest"] = MainQuest.objects.all()
    event_context["main_block"] = MainBlock.objects.all()
    event_context["events"] = Events.objects.all()
    return render(request, template_name='content.html', context=event_context)

