# Generated by Django 3.2.9 on 2021-11-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20211108_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='game_played',
            field=models.BooleanField(default=False),
        ),
    ]
