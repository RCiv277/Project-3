# Generated by Django 3.0.1 on 2020-01-01 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20200101_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='days',
            name='monday',
        ),
    ]