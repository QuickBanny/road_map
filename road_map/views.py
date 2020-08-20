from django.shortcuts import render
from django.http import response
from .models import MainQuest, MainBlock, Events
# Create your views here.


def first(request):
    event_context = {"quest_name": {"block_name1": ["event1", "event2"],
                                    "block_name2": ["event1", "event2"]},
                     "quest_name2": {"block_name1": ["event1", "event2"],
                                     "block_name2": ["event1", "event2"]}
                     }

    dick_quests = {}
    quests = MainQuest.objects.all()
    blocks = MainBlock.objects.all()
    for quest in quests:
        event_by_quest = Events.objects.filter(quest__name=quest.name)
        dick_blocks = {}
        for block in blocks:
            event_by_block = event_by_quest.filter(block__name=block.name)
            dick_blocks[block.name] = event_by_block
        dick_quests[quest.name] = dick_blocks

    return render(request, template_name='content.html', context={'context': dick_quests,
                                                                  'quests': quests,
                                                                  'blocks': blocks})

