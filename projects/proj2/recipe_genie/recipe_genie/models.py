from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(db_index=True)
    def __unicode__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=200, db_index=True, primary_key=True)
    recipes = models.ManyToManyField(Recipe)
    def __unicode__(self):
        return self.name
