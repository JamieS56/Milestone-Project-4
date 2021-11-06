# Generated by Django 3.2.9 on 2021-11-04 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20211103_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='away_team',
        ),
        migrations.AddField(
            model_name='fixture',
            name='away_team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='teams.team'),
        ),
        migrations.RemoveField(
            model_name='fixture',
            name='home_team',
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.team'),
        ),
    ]
