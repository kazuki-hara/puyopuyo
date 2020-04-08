from django.db import models

# Create your models here.
class Result(models.Model):
    username = models.CharField(max_length=20)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)