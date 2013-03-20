import urllib2
import json

def get_titles_and_urls_on_page(url):
    html = urllib2.urlopen(url)
    titles_and_urls = []
    for line in html:
        begin_offset = len('RecipeTitle" href="')
        if 'RecipeTitle" href="' in line:
            begin_url_index = line.find('RecipeTitle" href="') + begin_offset
            end_url_index = line[begin_url_index :].find('">') + begin_url_index
            url = line[begin_url_index : end_url_index]
            begin_title_index = end_url_index + 2
            end_title_index = line[begin_title_index:].find('<') + begin_title_index
            title = line[begin_title_index:end_title_index]
            titles_and_urls.append({'title' : title, 'url' : url})
    return titles_and_urls
            

#The code below gets all of titles and urls of recipes on the page 'http://allrecipes.com/recipes/ViewAll.aspx?Page=' and writes it to the file some_urls.json
titles_and_urls = get_titles_and_urls_on_page('http://allrecipes.com/recipes/ViewAll.aspx?Page=')
file_to_write_to = open('some_urls.json', 'w')
titles_and_urls_string = json.dumps(titles_and_urls)
file_to_write_to.write(titles_and_urls_string)
file_to_write_to.close()




#The code below is very similar to the code above but it gets the titles and urls for recipes on over two thousand html pages instead of just a single page and stores this in all_urls.json.
"""
base_url = 'http://allrecipes.com/recipes/ViewAll.aspx?Page='
all_titles_and_urls = []
for i in range(0, 2191):
    print i
    try:
        titles_and_urls = get_titles_and_urls_on_page(base_url + str(i))
        for title_and_url in titles_and_urls:
            all_titles_and_urls.append(title_and_url)
    except:
        print "error on ", base_url, i

file_to_write_to = open('all_urls.json', 'w')
all_titles_and_urls_string = json.dumps(all_titles_and_urls)
file_to_write_to.write(all_titles_and_urls_string)
file_to_write_to.close()
"""
