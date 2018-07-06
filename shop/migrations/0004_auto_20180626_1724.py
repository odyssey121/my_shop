# Generated by Django 2.0.6 on 2018-06-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180626_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Some',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('detail', models.PositiveIntegerField(verbose_name='На складе')),
                ('check', models.BooleanField(default=True, verbose_name='Доступен')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
