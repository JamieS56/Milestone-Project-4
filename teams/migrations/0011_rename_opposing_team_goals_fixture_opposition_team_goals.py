# Generated by Django 3.2.9 on 2021-11-09 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_alter_fixture_opposition_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='opposing_team_goals',
            new_name='opposition_team_goals',
        ),
    ]