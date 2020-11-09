from django.shortcuts import render
from django.http import response
from .models import Level, MainBlock, Events
# Create your views here.


def first(request):
    dict_quests = {}
    #quests = Level.objects.all()
    quests = Level.objects.order_by('position')

    blocks = MainBlock.objects.all()
    for quest in quests:
        finished_pers = 0
        event_by_quest = Events.objects.filter(quest__name=quest.name)
        event_by_quest_finished = Events.objects.filter(quest__name=quest.name, finished=True)
        if event_by_quest_finished:
            finished_pers = (100 // len(event_by_quest)) * len(event_by_quest_finished)

        str_all_events = '{}/{}'.format(len(event_by_quest_finished), len(event_by_quest))
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
                                                     'finished_pers': finished_pers,
                                                     'str_all_events': str_all_events}

    return render(request, template_name='content.html', context={'context': dict_quests})

