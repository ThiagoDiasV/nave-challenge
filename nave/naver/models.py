from django.db import models
from nave.project.models import Project
from django.contrib.auth import get_user_model


class Naver(models.Model):
    user = models.OneToOneField(
        get_user_model(), verbose_name="User", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60, verbose_name="Naver name")
    birthdate = models.DateField(verbose_name="Birth date")
    admission_date = models.DateField(auto_now_add=True, verbose_name="Admission date")
    job_role = models.CharField(max_length=30, verbose_name="Job role")
    projects = models.ManyToManyField(
        Project, verbose_name="Projects", related_name="projects"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
