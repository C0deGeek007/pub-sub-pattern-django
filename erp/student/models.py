from django.db import models

# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=200)
    roll = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Student roll"
    )
