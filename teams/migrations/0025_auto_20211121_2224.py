# Generated by Django 3.2.9 on 2021-11-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0024_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='draws',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='losses',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]