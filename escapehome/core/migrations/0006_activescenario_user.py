# Generated by Django 2.1.5 on 2019-07-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190701_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='activescenario',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
