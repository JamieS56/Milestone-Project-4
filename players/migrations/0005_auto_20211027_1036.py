# Generated by Django 3.2.8 on 2021-10-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20211019_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='close_up_image_url',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='player',
            name='main_image_url',
        ),
    ]