# Generated by Django 4.2.7 on 2024-01-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourates', '0022_remove_juda_n_verset_juda_n_chap'),
    ]

    operations = [
        migrations.AddField(
            model_name='juda',
            name='n_verset',
            field=models.IntegerField(default=1),
        ),
    ]
