# Generated by Django 2.1.5 on 2019-07-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190716_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='protocol',
            field=models.CharField(choices=[('KNX', 'knx'), ('PHue', 'philips hue'), ('Modbus', 'modbus')], max_length=255),
        ),
    ]
