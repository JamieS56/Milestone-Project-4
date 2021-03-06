# Generated by Django 3.2.9 on 2021-11-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('teams', '0017_auto_20211116_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.fixture')),
                ('ticket_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TicketOrder',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_tickets', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
