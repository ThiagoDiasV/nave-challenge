from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="Project name")
    # naver = models.ManyToManyField(Naver)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
