# Generated by Django 4.2.1 on 2023-07-24 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extrato", "0008_alter_valores_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="valores",
            name="data",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 23, 21, 47, 27, 115609)
            ),
        ),
    ]
