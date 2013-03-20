from django.utils import simplejson as json

def find_recipes(ingredients):
    recipe_file = open('recipe_genie/static/all_recipes.json', 'r')
    all_recipes = json.loads(recipe_file.read())
    recipe_file.close()
    result_recipes = []
    for recipe_dict in all_recipes:
        has_all_ingredients = True
        for ingredient in ingredients:
            if ingredient not in recipe_dict['ingredients']:
                has_all_ingredients = False
        if has_all_ingredients:
            recipe = {'title': recipe_dict['title'], 'url': recipe_dict['url'], 'percent': 0}
            result_recipes.append(recipe)
    return result_recipes
