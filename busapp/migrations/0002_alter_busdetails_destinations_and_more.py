# Generated by Django 4.0 on 2022-02-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdetails',
            name='destinations',
            field=models.TextField(choices=[('1', 'Villupuram'), ('2', 'Chengalpattu'), ('3', 'Chennai')], default='3'),
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='ticket_costs',
            field=models.IntegerField(choices=[('1', '100'), ('2', '150'), ('3', '200')], default='3'),
        ),
    ]
