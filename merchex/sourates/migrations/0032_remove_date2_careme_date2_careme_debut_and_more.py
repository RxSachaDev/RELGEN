# Generated by Django 5.0.2 on 2024-02-12 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourates', '0031_date2_ramadan_debut_date2_ramadan_fin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date2',
            name='careme',
        ),
        migrations.AddField(
            model_name='date2',
            name='careme_debut',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='date2',
            name='careme_fin',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
