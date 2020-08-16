# Generated by Django 3.1 on 2020-08-16 18:09

import datetime

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20200816_1806"),
    ]

    operations = [
        migrations.AlterField(
            model_name="naver",
            name="admission_date",
            field=models.DateField(
                auto_now_add=True,
                validators=[
                    django.core.validators.MaxValueValidator(
                        limit_value=datetime.date(2020, 8, 16)
                    )
                ],
                verbose_name="Admission date",
            ),
        ),
        migrations.AlterField(
            model_name="naver",
            name="birthdate",
            field=models.DateField(
                validators=[
                    django.core.validators.MaxValueValidator(
                        limit_value=datetime.date(2020, 8, 16)
                    )
                ],
                verbose_name="Birth date",
            ),
        ),
    ]
