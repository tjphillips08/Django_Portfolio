from django.db import models

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    github = models.CharField(max_length=250)
    deploy = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']