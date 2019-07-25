from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.TextField(max_length=200, default="")
    summary = models.CharField(max_length=1000)
