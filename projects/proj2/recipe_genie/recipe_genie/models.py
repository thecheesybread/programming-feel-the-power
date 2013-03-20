from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    def __unicode__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe)
    def __unicode__(self):
        return self.name
