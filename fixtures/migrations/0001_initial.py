# Generated by Django 3.2.9 on 2021-11-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0010_auto_20211124_1827'),
        ('teams', '0025_auto_20211121_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('game_played', models.BooleanField(default=False)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='teams.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('assist_maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assists', to='players.player')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixtures.fixture')),
                ('goal_scorer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='players.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_goals', to='teams.team')),
            ],
        ),
    ]
