from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class Naver(models.Model):
    """
    Naver model with user, name, birthdate, admission_date,
    job_role and projects fields.
    """

    user = models.OneToOneField(
        get_user_model(), verbose_name="User", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60, verbose_name="Naver name")
    birthdate = models.DateField(
        verbose_name="Birth date",
        validators=[MaxValueValidator(limit_value=date.today)],
    )
    admission_date = models.DateField(
        auto_now_add=True,
        verbose_name="Admission date",
        validators=[MaxValueValidator(limit_value=date.today)],
    )
    job_role = models.CharField(max_length=30, verbose_name="Job role")
    projects = models.ManyToManyField("Project", related_name="projects", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Project model with name and navers fields.
    """

    name = models.CharField(max_length=50, verbose_name="Project name")
    navers = models.ManyToManyField("Naver", through="Naver_projects", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
