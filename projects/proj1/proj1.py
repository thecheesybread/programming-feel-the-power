import urllib2
import json
file_to_read_from = open('all_urls.json', 'r')
all_titles_and_urls = json.loads(file_to_read_from.read())
file_to_read_from.close()


some_titles_and_urls = [{"url": "http://allrecipes.com/recipe/-applesauce-pumpkin-bread/detail.aspx", "title": " Applesauce Pumpkin Bread"}, {"url": "http://allrecipes.com/recipe/-banana-peanut-butter-cheesecake-aka-the-elvis/detail.aspx", "title": " Banana Peanut Butter Cheesecake aka &#34;The Elvis&#34;"}, {"url": "http://allrecipes.com/recipe/bowl-full-of-cherry-ham-glaze/detail.aspx", "title": "&#34;Bowl Full of Cherry&#34; Ham Glaze"}, {"url": "http://allrecipes.com/recipe/couldnt-be-easier-three-bean-salad/detail.aspx", "title": "&#34;Couldn't Be Easier&#34; Three-Bean Salad"}, {"url": "http://allrecipes.com/recipe/fruit-smoothie-no-bake-cheesecake-from-philadelphia/detail.aspx", "title": "&#34;Fruit Smoothie&#34; No-Bake Cheesecake from PHILADELPHIA&#174;"}, {"url": "http://allrecipes.com/recipe/million-dollar-chinese-cabbage-salad/detail.aspx", "title": "&#34;Million Dollar&#34; Chinese Cabbage Salad  "}, {"url": "http://allrecipes.com/recipe/pantry-raid-chicken-enchilada-casserole/detail.aspx", "title": "&#34;Pantry Raid&#34; Chicken Enchilada Casserole"}, {"url": "http://allrecipes.com/recipe/spactacular-frozen-grapes/detail.aspx", "title": "&#34;Spa&#34;ctacular Frozen Grapes"}, {"url": "http://allrecipes.com/recipe/zuccotto-cupcakes/detail.aspx", "title": "&#34;Zuccotto&#34; Cupcakes"}, {"url": "http://allrecipes.com/recipe/1-pea-salad-most-requested/detail.aspx", "title": "#1 Pea Salad Most Requested!"}, {"url": "http://allrecipes.com/recipe/1-pumpkin-spice-cookies/detail.aspx", "title": "#1 Pumpkin Spice Cookies"}, {"url": "http://allrecipes.com/recipe/gluten-free-magic-cookie-bars/detail.aspx", "title": "(Gluten Free) Magic Cookie Bars"}, {"url": "http://allrecipes.com/recipe/10-pound-cheesecake/detail.aspx", "title": "10 Pound Cheesecake"}, {"url": "http://allrecipes.com/recipe/100-percent-whole-wheat-bread/detail.aspx", "title": "100 Percent Whole Wheat Bread"}, {"url": "http://allrecipes.com/recipe/100-fruit-cake/detail.aspx", "title": "100% Fruit &#34;Cake&#34;"}, {"url": "http://allrecipes.com/recipe/10-minute-tomato-basil-salad/detail.aspx", "title": "10-Minute Tomato Basil Salad"}, {"url": "http://allrecipes.com/recipe/120-calorie-peach-pies/detail.aspx", "title": "120 Calorie Peach Pies"}, {"url": "http://allrecipes.com/recipe/121-whipped-cream/detail.aspx", "title": "121 Whipped Cream"}, {"url": "http://allrecipes.com/recipe/123-green-tea-ice-cream/detail.aspx", "title": "123 Green Tea Ice Cream"}, {"url": "http://allrecipes.com/recipe/1-2-3-jambalaya/detail.aspx", "title": "1-2-3 Jambalaya"}]



#Given a url for a recipe and the title of the recipe
def get_ingredients(url, title):
    html = urllib2.urlopen(url)
    result = {}
    result['title'] = title
    ingredient_list = []
    #fill this out
    




    #fill this out
    result['ingredients'] = ingredient_list
    return result


print get_ingredients('http://allrecipes.com/recipe/apple-crisp-ii/detail.aspx', 'Apple Crisp II')




    
