import json

from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Device(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.get_child().__str__()

    def get_child(self):
        if hasattr(self, 'huelamp'):
            return self.huelamp
        if hasattr(self, 'hueremotecontrol'):
            return self.hueremotecontrol
        if hasattr(self, 'knxlamp'):
            return self.knxlamp
        if hasattr(self, 'knxshutter'):
            return self.knxshutter

    def get_id(self):
        device = self.get_child()
        if isinstance(device, HueLamp):
            return device.lamp_id
        if isinstance(device, HueRemoteControl):
            return device.control_id
        if isinstance(device, KNXLamp):
            return device.group_adddress


class HueLamp(Device):
    lamp_id = models.IntegerField()
    name = models.CharField(max_length=255)
    room = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'HueLamp {self.lamp_id} - {self.name} in {self.room}'


class HueRemoteControl(Device):
    control_id = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'HueRemoteControl {self.control_id} - {self.name}'


class KNXLamp(Device):
    group_adddress = models.CharField(max_length=255)

    def __str__(self):
        return f'KNXLamp {self.group_adddress}'


class KNXShutter(Device):

    def __str__(self):
        return f'KNXShutter {self.id}'


class Action(models.Model):
    name = models.CharField(primary_key=True, max_length=255, unique=True)
    function = models.CharField(max_length=255)
    parameters = models.TextField(help_text='als dict', blank=True, null=True)

    def __str__(self):
        return f'Action {self.name}'


class Command(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    actions = models.ManyToManyField(Action, through='OrderedAction', related_name='action', blank=True)
    devices = models.ManyToManyField(Device, related_name='device', blank=True)

    def __str__(self):
        return f'Command {self.name}'


class OrderedAction(models.Model):
    action = models.ForeignKey(Action, on_delete=models.DO_NOTHING)
    command = models.ForeignKey(Command, on_delete=models.DO_NOTHING)
    order = models.IntegerField()

    class Meta:
        ordering = ['order', ]


class Riddle(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.TextField()
    solution = models.TextField()
    points = models.IntegerField()
    commands = models.ManyToManyField(Command, blank=True, related_name='riddle')
    hints = models.TextField(blank=True)
    correct = models.TextField(blank=True, default="Grandios, dass war richtig.")
    incorrect = models.TextField(blank=True, default="Schade, dass war leider falsch, versuch es doch nochmal.")

    class Meta:
        verbose_name_plural = "Riddles"

    def __str__(self):
        return f'Riddle {self.id} - {self.task}'


class Scenario(models.Model):
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    DIFFICULT = 'DIFFICULT'

    STATUS_CHOICES = (
        (EASY, 'Leicht'),
        (MEDIUM, 'Mittel'),
        (DIFFICULT, 'Schwer'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    riddles = models.ManyToManyField(Riddle, related_name='scenario')
    severity = models.CharField(max_length=255, default=MEDIUM, choices=STATUS_CHOICES, blank=True)
    length = models.DurationField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Scenarios"

    def __str__(self):
        return self.name

    @property
    def possible_points(self):
        return self.riddles.aggregate(Sum('points'))['points__sum']


class ActiveScenario(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.DO_NOTHING, related_name='active_scenarios', blank=True,
                                 null=True)
    riddle = models.ForeignKey(Riddle, on_delete=models.DO_NOTHING, related_name='active_riddles', blank=True,
                               null=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    players = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    score = models.IntegerField(default=0)
    state = models.IntegerField(blank=True, null=True)


@receiver(post_save, sender=Riddle)
def sync_slottype_riddle(sender, instance, **kwargs):
    _sync(sender.__name__, instance.solution)


@receiver(post_save, sender=Scenario)
def sync_slottype_scenario(sender, instance, **kwargs):
    _sync(sender.__name__, instance.other_names)


def _sync(model_name, types):
    types = types.split(', ') if ', ' in types else [types]
    model_path = f'{settings.STATIC_ROOT}/model.json'

    skill_model = json.loads(open(model_path).read())
    for slot_type in skill_model['interactionModel']['languageModel']['types']:
        if slot_type['name'] == f'ESCAPEHOME_{model_name}':
            for value in types:
                if {'name': {'value': value}} not in slot_type['values']:
                    slot_type['values'].append({'name': {'value': value}})

    with open(model_path, 'w', encoding='utf-8') as json_file:
        json.dump(skill_model, json_file, ensure_ascii=False, indent=2)
