# Generated by Django 5.0.2 on 2024-02-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourates', '0029_sourate_arabe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juda_hebreu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3000)),
                ('verset', models.CharField(max_length=5000)),
                ('n_verset', models.IntegerField(default=1)),
                ('n_chap', models.IntegerField(default=1)),
            ],
        ),
    ]
