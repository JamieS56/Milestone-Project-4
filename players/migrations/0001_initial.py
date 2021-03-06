# Generated by Django 3.2.8 on 2021-10-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('apearences', models.IntegerField()),
                ('position', models.CharField(max_length=15)),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('clean_sheets', models.IntegerField()),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
