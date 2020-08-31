from django.shortcuts import render
from django.http import response
from .models import MainQuest, MainBlock, Events
# Create your views here.


def first(request):
    dict_quests = {}
    quests = MainQuest.objects.all()
    blocks = MainBlock.objects.all()
    for quest in quests:
        event_by_quest = Events.objects.filter(quest__name=quest.name)
        dict_blocks = {}
        for block in blocks:
            event_by_block = event_by_quest.filter(block__name=block.name).order_by('finished')
            finished_event_by_block = event_by_quest.filter(block__name=block.name, finished=True)
            if not finished_event_by_block:
                finished_pers = 0
            else:
                finished_pers = (100/len(event_by_block))*len(finished_event_by_block)
            dict_blocks[block.name.replace(' ', '_')] = {'id': block.id,
                                                         'name': block.name,
                                                         'dead_line': block.dead_line,
                                                         'events': event_by_block,
                                                         'finished_block': finished_pers,
                                                         'count_events': len(event_by_block)}
        dict_quests[quest.name.replace(' ', '_')] = {'id': quest.id,
                                                     'name': quest.name,
                                                     'blocks': dict_blocks}

    return render(request, template_name='content.html', context={'context': dict_quests})

