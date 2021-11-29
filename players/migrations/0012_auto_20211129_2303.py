# Generated by Django 3.2.9 on 2021-11-29 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0011_auto_20211124_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Goalkeeper', 'Goalkeeper'), ('Defender', 'Defender'), ('Midfield', 'Midfield'), ('Forward', 'Forward')], max_length=15),
        ),
    ]
