# Generated by Django 4.2.1 on 2023-07-24 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extrato", "0029_alter_valores_banco_alter_valores_categoria_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="valores",
            name="data",
            field=models.DateField(
                default=datetime.datetime(2023, 7, 24, 0, 38, 15, 490796)
            ),
        ),
    ]