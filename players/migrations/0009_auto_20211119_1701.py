# Generated by Django 3.2.9 on 2021-11-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20211119_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='apearences',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='clean_sheets',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]