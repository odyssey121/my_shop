# Generated by Django 2.0.6 on 2018-06-27 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180627_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='some',
            old_name='title',
            new_name='slug',
        ),
    ]
