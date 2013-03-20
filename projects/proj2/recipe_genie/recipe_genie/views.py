from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.utils import simplejson as json
from models import Recipe, Ingredient
from django.db.models import Q
from django.http import HttpResponse
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


ingredient_list = ['clove', 'breadnut', 'kale', 'vanilla', 'buckwheat', 'sage', 'nasturtium', 'chickpea', 'turnip', 'egg', 'blueberry', 'jimbu', 'tinda', 'coconut', 'scallop', 'shallot', 'passion fruit', 'plum', 'pig', 'quinoa', 'artichoke', 'jujube', 'mung bean', 'barley', 'pepper', 'rye', 'peach', 'spinach', 'cardamom', 'apricot', 'safflower', 'saffron', 'bison', 'fig', 'giant gourami', 'collard greens', 'trout', 'butter', 'cilantro', 'oil', 'oats', 'cicely', 'raisin', 'fennel', 'sugar', 'water', 'horseradish', 'oatmeal', 'buffaloberry', 'mustard', 'macadamia', 'lima bean', 'zucchini', 'chestnut', 'pork', 'pheasant', 'pear', 'squash', 'parsnip', 'kaffir lime', 'carrot', 'asparagus', 'butter bean', 'edadame', 'golpar', 'tomatillo', 'tomato', 'peanut', 'peppermint', 'borage', 'baking cocoa', 'pumpkin', 'vegetable oil', 'mastic', 'almond', 'grape', 'anise', 'cumin', 'winter melon', 'cuban oregano', 'black bean', 'sweet potato', 'cress', 'persimmon', 'lime', 'rice', 'wheat', 'beef', 'potato', 'calico bean', 'elderberry', 'amaranth', 'grapefruit', 'beet', 'flour', 'catfish', 'chive', 'marjoram', 'dill seed', 'thyme', 'rhubarb', 'fish', 'coffee', 'mulberry', 'mango', 'pineapple', 'popcorn', 'lentil', 'shrimp', 'baking soda', 'vanilla extract', 'clam', 'apple', 'cherry', 'cashew', 'juniper berry', 'cardoon', 'milk', 'parsley', 'clarias', 'pecan', 'onion', 'orange', 'curry leaf', 'skirret', 'salt', 'coriander', 'lamb', 'hickory', 'boldo', 'corn', 'lavender', 'cannellini bean', 'cowpea', 'pomelo', 'cubeb', 'bitter melon', 'cucumber', 'mussel', 'ground pepper', 'watercress', 'mint', 'cabbage', 'oyster', 'lemongrass', 'pinto bean', 'split pea', 'gooseberry', 'dragonfruit', 'black-eyed bean', 'chickweed', 'walnut', 'arugula', 'chokeberry', 'catnip', 'nutmeg', 'blackberry', 'eggplant', 'bamboo', 'rosemary', 'banana', 'raspberry', 'yam', 'quail', 'bell pepper', 'salmon', 'lemon', 'kidney bean', 'nectarine', 'brown rice', 'duck', 'avocado', 'italian bean', 'date', 'navy bean', 'cattle', 'basil', 'kala zeera', 'baking powder', 'lemon balm', 'turkey', 'cauliflower', 'broccoli', 'lettuce', 'lobster', 'cinnamon', 'soybean', 'galangal', 'sweet pepper', 'flaxseed', 'guava', 'carp', 'papaya', 'radish', 'pistachio', 'mace', 'garlic', 'ginger', 'hazelnut', 'chicken', 'elephant garlic', 'chicory', 'scallion', 'taro', 'tilapia', 'kawakawa', 'prawn', 'celery', 'strawberry', 'venison', 'crab', 'kencur', 'leek', 'chocolate', 'caramel', 'sugar', 'salt', 'pepper']
ingredient_set = set(ingredient_list)
def get_recipes(request):
    #json_data = json.loads(request.raw_post_data)
    #ingredients = json_data['ingredients']
    ingredients = ['chicken', 'garlic']
    q = Q()
    for ingredient in ingredients:
        ingredient = ingredient.lower().strip()
        try:
            ingredient_obj = Ingredient.objects.get(name=ingredient)
            q &= Q(ingredient__name=ingredient)
        except:
            pass
    print q
    print Recipe.objects.filter(ingredient__name=q)
    #print Recipe.objects.filter(q)[1]
    #print Recipe.objects.filter(q)[2]
    return HttpResponse("Success")
