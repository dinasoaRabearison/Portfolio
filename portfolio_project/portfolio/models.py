from django.db import models

# Create your models here.
class My_User(models.Model):
    nom = models.CharField(max_length=60)
    poste = models.CharField(max_length=150)
    observation = models.CharField(max_length=200)
    date_inscription = models.DateField()