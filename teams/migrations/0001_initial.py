# Generated by Django 3.2.9 on 2021-11-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_goals', models.IntegerField(blank=True)),
                ('away_team_goals', models.IntegerField(blank=True)),
                ('teams', models.ManyToManyField(to='teams.Team')),
            ],
        ),
    ]
