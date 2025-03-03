from django.db import models

# data base model for item app categories

class Category(models.Model):
    #models goes here!
    name = models.CharField(max_length=255)
