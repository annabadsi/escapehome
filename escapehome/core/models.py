import json

from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Device(models.Model):
    id = models.AutoField(primary_key=True)


class Lamp(Device):
    RED = 'RED'
    ORGANGE = 'ORGANGE'
    YELLOW = 'YELLOW'
    BLUE = 'BLUE'
    MAGENTA = 'MAGENTA'
    CYAN = 'CYAN'
    GREEN = 'GREEN'
    WHITE = 'WHITE'

    COLOR_CHOICES = (
        ('FF00FF', MAGENTA),
        ('ff0000', RED),
        ('ffa500', ORGANGE),
        ('f5ff00', YELLOW),
        ('0000ff', BLUE),
        ('00ffff', CYAN),
        ('00f700', GREEN),
        ('ffffff', WHITE),
    )

    lamp_id = models.IntegerField()
    name = models.CharField(max_length=255)
    on = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default=WHITE, choices=COLOR_CHOICES, help_text='hex-value, default white')
    room = models.CharField(max_length=255, blank=True)
    brightness = models.IntegerField(default=254, blank=True, help_text='254 = 100%, 127 = 50%, ...')

    def __str__(self):
        return f'Lamp {self.id} - {self.name} in {self.room}'


class Command(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    function = models.CharField(max_length=255)
    config = models.TextField(help_text='in JSON')
    devices = models.ManyToManyField(Device, blank=True, related_name='device')

    def __str__(self):
        return f'Command {self.id} - {self.name}'


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
