# Generated by Django 5.0.7 on 2024-07-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_engine_condition_alter_engine_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='engine',
            name='price_order',
            field=models.FloatField(default=0),
        ),
    ]
