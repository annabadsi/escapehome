# Generated by Django 2.1.5 on 2019-07-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190706_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='other_names',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
