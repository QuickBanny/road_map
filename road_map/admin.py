from django.contrib import admin

from .models import Category, Status, MainBlock, MainQuest, Events
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(MainQuest)
class MainQuestAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'block', 'category', 'status', 'main_img',)