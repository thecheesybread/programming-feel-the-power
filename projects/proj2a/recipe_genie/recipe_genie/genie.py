from django.utils import simplejson as json

def find_recipes(specified_ingredients):
    recipe_file = open('data/all_recipes.json', 'r')
    all_recipes = json.loads(recipe_file.read())
    recipe_file.close()

    # FILL THIS IN
    # Clearly what is below is not correct
    some_recipe = {'title': 'Some Recipe Title',
        'url': 'http://allrecipes.com/recipe/some-recipe/detail.aspx',
        'percent': 47
    }
    some_other_recipe = {
        'title': 'Some Other Recipe Title',
        'url': 'http://allrecipes.com/recipe/some-other-recipe/detail.aspx',
        'percent': 23
    }
    result_recipes = [some_recipe, some_other_recipe]

    return result_recipes
