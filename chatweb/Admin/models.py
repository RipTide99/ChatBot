from django.db import models

# Create your models here.
class Query_table(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()

class admission(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()

class canteen(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()