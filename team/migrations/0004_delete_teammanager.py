# Generated by Django 4.0.4 on 2023-10-19 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_teammanager_team_members_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamManager',
        ),
    ]
