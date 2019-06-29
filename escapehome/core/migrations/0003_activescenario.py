# Generated by Django 2.1.5 on 2019-06-23 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190617_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.IntegerField(blank=True, null=True)),
                ('duration', models.DurationField()),
                ('score', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='active_scenarios', to='core.Scenario')),
            ],
        ),
    ]
