# Generated by Django 2.1.5 on 2019-06-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_activescenario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activescenario',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]