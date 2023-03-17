# Generated by Django 4.0 on 2022-02-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0006_alter_busdetails_destinations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busdetails',
            name='persons',
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='destinations',
            field=models.TextField(choices=[(0, 'Villupuram'), (1, 'Chengalpattu'), (2, 'Chennai')], default=2),
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='ticket_costs',
            field=models.IntegerField(choices=[(0, 100), (1, 150), (2, 200)], default=2),
        ),
    ]
