import urllib2
import json
base_url = 'http://allrecipes.com/recipes/ViewAll.aspx?Page='
all_titles_and_urls = []
def get_titles_and_urls_on_page(url):
    response = urllib2.urlopen(url)
    titles_and_urls = []
    for line in response:
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
            
titles_and_urls = get_titles_and_urls_on_page(base_url + '1')
with open('small_urls.json', 'w') as outfile:
  json.dump(titles_and_urls, outfile)


for i in range(0, 2191):
    print i
    try:
        titles_and_urls = get_titles_and_urls_on_page(base_url + str(i))
        for title_and_url in titles_and_urls:
            all_titles_and_urls.append(title_and_url)
    except:
        print "error on ", base_url, i

with open('all_urls.json', 'w') as outfile:
  json.dump(all_titles_and_urls, outfile)
