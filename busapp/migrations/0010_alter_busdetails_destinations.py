# Generated by Django 4.0 on 2022-02-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0009_alter_busdetails_destinations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdetails',
            name='destinations',
            field=models.TextField(choices=[('Villupuram', 'Villupuram'), ('Chengalpattu', 'Chengalpattu'), ('Chennai', 'Chennai')], default='Chennai'),
        ),
    ]