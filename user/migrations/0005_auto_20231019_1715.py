# Generated by Django 4.0.4 on 2023-10-19 14:15

from django.core.management import call_command
from django.db import migrations


def func(apps, schema_editor):
    call_command("loaddata", "fixture_data.json")


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_user_first_name_alter_user_last_name"),
    ]

    operations = [
        migrations.RunPython(func, reverse_func),
    ]
