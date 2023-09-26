from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created = models.DateField()

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)