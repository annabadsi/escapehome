# Generated by Django 2.1.5 on 2019-07-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190703_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riddle',
            old_name='code',
            new_name='points',
        ),
    ]
