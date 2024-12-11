from django.db import models

# Create your models here.
class Game(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    place=models.CharField(max_length=30)
    thing=models.CharField(max_length=30)
    number=models.IntegerField()



