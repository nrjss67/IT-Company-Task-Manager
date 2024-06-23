from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=100)


class Position(models.Model):
    name = models.CharField(max_length=100)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Task(models.Model):

    class Priorety(models.TextChoices):
        L = "L", "Low"
        M = "M", "Medium"
        H = "H", "High"
        C = "C", "Critical"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    deadline = models.DateField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(choices=Priorety.choices, default=Priorety.L, max_length=1)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)
