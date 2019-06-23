from django.contrib import admin

from core.models import *


@admin.register(Scenario)
class ScenariosAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'description',
        'severity',
    ]

    list_display = (
        'name',
        'severity',
        'show_riddles',
    )

    def show_riddles(self, obj: Scenario):
        return [riddle.get('task') for riddle in obj.riddles.values('task')]


@admin.register(ActiveScenario)
class ActiveScenarioAdmin(admin.ModelAdmin):
    search_fields = [
        'scenario__name',
    ]

    list_display = (
        'get_scenario',
        'duration',
        'score',
        'state'
    )

    def get_scenario(self, obj: ActiveScenario):
        return obj.scenario.name


@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    search_fields = [
        'task',
        'solution',
        'code',
    ]

    list_display = (
        'id',
        'task',
        'solution',
        'show_commands',
        'code',
    )

    def show_commands(self, obj):
        return [riddle.get('name') for riddle in obj.commands.values('name')]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )


@admin.register(Lamp)
class LampAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = (
        'name',
        'room',
        'brightness',
        'color',
    )


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = (
        'name',
    )
