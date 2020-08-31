from django.shortcuts import render
from django.http import response
from .models import MainQuest, MainBlock, Events
# Create your views here.


def first(request):
    dict_quests = {}
    quests = MainQuest.objects.all()
    blocks = MainBlock.objects.all()
    for quest in quests:
        finished_pers = 0
        event_by_quest = Events.objects.filter(quest__name=quest.name)
        event_by_quest_finished = Events.objects.filter(quest__name=quest.name, finished=True)
        if event_by_quest_finished:
            finished_pers = (100 // len(event_by_quest)) * len(event_by_quest_finished)

        dict_blocks = {}
        for block in blocks:
            event_by_block = event_by_quest.filter(block__name=block.name).order_by('finished')
            dict_blocks[block.name.replace(' ', '_')] = {'id': block.id,
                                                         'name': block.name,
                                                         'events': event_by_block,
                                                         'count_events': len(event_by_block)}
        dict_quests[quest.name.replace(' ', '_')] = {'id': quest.id,
                                                     'name': quest.name,
                                                     'date_of_release': quest.date_of_release,
                                                     'blocks': dict_blocks,
                                                     'finished_pers': finished_pers}

    return render(request, template_name='content.html', context={'context': dict_quests})

