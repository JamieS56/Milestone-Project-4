# Generated by Django 3.2.9 on 2021-11-11 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_player_managers'),
        ('teams', '0011_rename_opposing_team_goals_fixture_opposition_team_goals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='opposition_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('assist_maker', models.ManyToManyField(related_name='assist_maker', to='players.Player')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.fixture')),
                ('goal_scorer', models.ManyToManyField(related_name='goal_scorer', to='players.Player')),
            ],
        ),
    ]
