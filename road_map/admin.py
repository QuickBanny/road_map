from django.contrib import admin

from .models import Status, MainBlock, Level, Events
# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Level)
class MainQuestAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'position')


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'quest', 'block', 'status', 'main_img')