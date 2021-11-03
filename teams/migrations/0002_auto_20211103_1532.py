# Generated by Django 3.2.9 on 2021-11-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='teams',
        ),
        migrations.AddField(
            model_name='fixture',
            name='away_team',
            field=models.ManyToManyField(related_name='away_team', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_team',
            field=models.ManyToManyField(related_name='home_team', to='teams.Team'),
        ),
    ]
