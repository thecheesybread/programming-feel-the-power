import json
from recipe_genie.models import Recipe, Ingredient

ingredients_file = open('data/recipe_ingredients.json', 'r')
all_recipe_ingredients = json.loads(ingredients_file.read())
ingredients_file.close()
for recipe_dict in all_recipe_ingredients:

    url = recipe_dict['url']
    title = recipe_dict['title']
    ingredients = recipe_dict['ingredients']
    if len(Recipe.objects.filter(url=url)) > 0:
        continue
    new_recipe = Recipe(title=title, url=url)
    new_recipe.save()
    for ingredient in ingredients:
        ingredient = ingredient.lower()
        try:
            ingredient_obj = Ingredient.objects.get(name=ingredient)
        except Ingredient.DoesNotExist:
            ingredient_obj = Ingredient(name=ingredient)
            ingredient_obj.save()#need to call this before or else will return error

        ingredient_obj.recipes.add(new_recipe)
        ingredient_obj.save()
