# Generated by Django 2.2.7 on 2019-12-04 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_auto_20191205_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaorder',
            name='number',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
