from django.db import models
from django.db.models import Sum


class Device(models.Model):
    id = models.AutoField(primary_key=True)


class Lamp(Device):
    lamp_id = models.IntegerField()
    name = models.CharField(max_length=255)
    on = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default='#ffffff', help_text='hex-value, default white')
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
    code = models.IntegerField()
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
    description = models.TextField(blank=True)
    riddles = models.ManyToManyField(Riddle, related_name='scenario')
    severity = models.CharField(max_length=255, default=MEDIUM, choices=STATUS_CHOICES, blank=True)
    length = models.DurationField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Scenarios"

    def __str__(self):
        return f'Scenario {self.id} - {self.name}'

    @property
    def possible_points(self):
        return self.riddles.aggregate(Sum('code'))['code__sum']


class ActiveScenario(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.DO_NOTHING, related_name='active_scenarios', blank=True, null=True)
    riddle = models.ForeignKey(Riddle, on_delete=models.DO_NOTHING, related_name='active_riddles', blank=True, null=True)
    user = models.CharField(max_length=255, null=True)
    players = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    score = models.IntegerField(default=0)
    state = models.IntegerField(blank=True, null=True)
