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
        'id',
        'get_scenario',
        'duration',
        'score',
        'state'
    )

    def get_scenario(self, obj: ActiveScenario):
        return obj.scenario.name if obj.scenario else ''


@admin.register(Riddle)
class RiddleAdmin(admin.ModelAdmin):
    search_fields = [
        'task',
        'solution',
        'points',
    ]

    list_display = (
        'id',
        'task',
        'solution',
        'show_commands',
        'points',
    )

    def show_commands(self, obj):
        return [riddle.get('name') for riddle in obj.commands.values('name')]


@admin.register(HueLamp)
class HueLampAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = (
        'lamp_id',
        'name',
        'room',
    )


@admin.register(HueRemoteControl)
class HueRemoteControlAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = (
        'control_id',
        'name',
    )


@admin.register(KNXLamp)
class KNXLampAdmin(admin.ModelAdmin):
    pass


@admin.register(ModbusMotor)
class ModbusMotor(admin.ModelAdmin):
    pass


class OrderedActionActionAdmin(admin.TabularInline):
    model = OrderedAction
    extra = 1  # how many rows to show


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    inlines = (
        OrderedActionActionAdmin,
    )

    search_fields = [
        'name',
    ]

    list_display = (
        'name',
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = (
        'name',
        'function'
    )
