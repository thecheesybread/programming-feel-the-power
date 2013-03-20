import json
from recipe_genie.models import Recipe, Ingredient

ingredient_list = ['clove', 'breadnut', 'kale', 'vanilla', 'buckwheat', 'sage', 'nasturtium', 'chickpea', 'turnip', 'egg', 'blueberry', 'jimbu', 'tinda', 'coconut', 'scallop', 'shallot', 'passion fruit', 'plum', 'pig', 'quinoa', 'artichoke', 'jujube', 'mung bean', 'barley', 'pepper', 'rye', 'peach', 'spinach', 'cardamom', 'apricot', 'safflower', 'saffron', 'bison', 'fig', 'giant gourami', 'collard greens', 'trout', 'butter', 'cilantro', 'oil', 'oats', 'cicely', 'raisin', 'fennel', 'sugar', 'water', 'horseradish', 'oatmeal', 'buffaloberry', 'mustard', 'macadamia', 'lima bean', 'zucchini', 'chestnut', 'pork', 'pheasant', 'pear', 'squash', 'parsnip', 'kaffir lime', 'carrot', 'asparagus', 'butter bean', 'edadame', 'golpar', 'tomatillo', 'tomato', 'peanut', 'peppermint', 'borage', 'baking cocoa', 'pumpkin', 'vegetable oil', 'mastic', 'almond', 'grape', 'anise', 'cumin', 'winter melon', 'cuban oregano', 'black bean', 'sweet potato', 'cress', 'persimmon', 'lime', 'rice', 'wheat', 'beef', 'potato', 'calico bean', 'elderberry', 'amaranth', 'grapefruit', 'beet', 'flour', 'catfish', 'chive', 'marjoram', 'dill seed', 'thyme', 'rhubarb', 'fish', 'coffee', 'mulberry', 'mango', 'pineapple', 'popcorn', 'lentil', 'shrimp', 'baking soda', 'vanilla extract', 'clam', 'apple', 'cherry', 'cashew', 'juniper berry', 'cardoon', 'milk', 'parsley', 'clarias', 'pecan', 'onion', 'orange', 'curry leaf', 'skirret', 'salt', 'coriander', 'lamb', 'hickory', 'boldo', 'corn', 'lavender', 'cannellini bean', 'cowpea', 'pomelo', 'cubeb', 'bitter melon', 'cucumber', 'mussel', 'ground pepper', 'watercress', 'mint', 'cabbage', 'oyster', 'lemongrass', 'pinto bean', 'split pea', 'gooseberry', 'dragonfruit', 'black-eyed bean', 'chickweed', 'walnut', 'arugula', 'chokeberry', 'catnip', 'nutmeg', 'blackberry', 'eggplant', 'bamboo', 'rosemary', 'banana', 'raspberry', 'yam', 'quail', 'bell pepper', 'salmon', 'lemon', 'kidney bean', 'nectarine', 'brown rice', 'duck', 'avocado', 'italian bean', 'date', 'navy bean', 'cattle', 'basil', 'kala zeera', 'baking powder', 'lemon balm', 'turkey', 'cauliflower', 'broccoli', 'lettuce', 'lobster', 'cinnamon', 'soybean', 'galangal', 'sweet pepper', 'flaxseed', 'guava', 'carp', 'papaya', 'radish', 'pistachio', 'mace', 'garlic', 'ginger', 'hazelnut', 'chicken', 'elephant garlic', 'chicory', 'scallion', 'taro', 'tilapia', 'kawakawa', 'prawn', 'celery', 'strawberry', 'venison', 'crab', 'kencur', 'leek', 'chocolate', 'caramel', 'sugar', 'salt', 'pepper']
ingredient_set = set(ingredient_list)




ingredients_file = open('data/recipe_ingredients_1000.json', 'r')
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
        ingredient_split = ingredient.split(' ')
        for sub_ingredient in ingredient_split:
            sub_ingredient = sub_ingredient.strip()
            #handle berries
            if 'berries' in sub_ingredient:
                sub_ingredient = sub_ingredient.replace('berries', 'berry')
            if sub_ingredient not in ingredient_set:
                continue
            try:
                ingredient_obj = Ingredient.objects.get(name=sub_ingredient)
            except Ingredient.DoesNotExist:
                ingredient_obj = Ingredient(name=sub_ingredient)
                ingredient_obj.save()#need to call this before or else will return error

            ingredient_obj.recipes.add(new_recipe)
            ingredient_obj.save()
