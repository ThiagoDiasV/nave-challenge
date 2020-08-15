# Generated by Django 3.1 on 2020-08-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_naver_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="naver",
            name="projects",
            field=models.ManyToManyField(
                blank=True, related_name="projects", to="api.Project"
            ),
        ),
    ]
