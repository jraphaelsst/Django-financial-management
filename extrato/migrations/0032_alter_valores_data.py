# Generated by Django 4.2.1 on 2023-07-24 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extrato", "0031_alter_valores_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="valores",
            name="data",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 24, 0, 57, 57, 460953)
            ),
        ),
    ]
