from django.utils import simplejson as json

def max_percent_recipe(recipes):
    max_percent = 0
    max_recipe = None
    for recipe in recipes:
        if recipe['percent'] > max_percent:
            max_percent = recipe['percent']
            max_recipe = recipe
    return max_recipe

def find_recipes(specified_ingredients):
    recipe_file = open('data/all_recipes.json', 'r')
    all_recipes = json.loads(recipe_file.read())
    recipe_file.close()
    unsorted_recipes = []
    for recipe_dict in all_recipes:
        num_ingredients = 0
        for ingredient in recipe_dict['ingredients']:
            if ingredient in specified_ingredients:
                num_ingredients += 1
        percent = 100 * num_ingredients / len(recipe_dict['ingredients'])
        if percent > 0:
            recipe = {'title': recipe_dict['title'], 'url': recipe_dict['url'], 'percent': percent}
            unsorted_recipes.append(recipe)

    sorted_recipes = []
    while len(unsorted_recipes) > 0:
        next_recipe = max_percent_recipe(unsorted_recipes)
        sorted_recipes.append(next_recipe)
        unsorted_recipes.remove(next_recipe)
    return sorted_recipes
