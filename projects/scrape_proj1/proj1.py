import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import sys

'''this is the wrapper file for project 1. fill these functions out'''

def identity(word):
    return word

def get_urls_on_page(url):
    http = httplib2.Http()
    header, content = http.request(url)
    all_urls = []
    for link in BeautifulSoup(content, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            all_urls.append(link['href'])
    return all_urls

def containsWord(url, word):
    h = httplib2.Http()
    header, content = h.request("http://reddit.com", "GET")
    print content
    if word in content:
        print True
    else:
        print False

def get_title(html):
    '''Given the html text of a craigslist post, returns the title'''
    #fill out here
    title = 'title'
    return title

def get_date(html):
    ''' Given the html text of a craigslist post, returns the date'''
    #fill out here
    date = 'date'
    return date

def get_price(html):
    ''' Given the html text of a craigslist post, returns the price'''
    #fill out here
    price = 'price'
    return price

def get_description(html):
    '''Given the html text of a craigslist post, returns the description'''
    #fill out here
    description = 'description'
    return description


def get_craigslist_info(url):
    '''Given the url of a craigslist post, gets the html and calls other functions that were defined to get the title, body, date, and description of the craigslist post'''
    http = httplib2.Http()
    header, html = http.request(url)
    print header
    title = get_title(html)
    date = get_date(html)
    price = get_price(html)
    description = get_description(html)
    info = {'title' : title, 'date' : date, 'price' : price, 'description' : description}
    return info

def collect_info():
    '''Given your assigned topic, write a script that returns a list of information dictionaries for that topic. An example below scrapes all information for berkeley apartments.'''
    pass

def collect_east_bay_apartments():
    http = httplib2.Http()
    base_url = 'http://sfbay.craigslist.org/eby/apa/'
    count = 0
    all_east_bay_apartments = []

    while True:
        if count == 0:
            current_url = base_url
        else:
            current_url = base_url + 'index' + str(count) + '.html'
        try:
            possible_ad_urls = get_urls_on_page(current_url)
        except:
            break
        '''when no more urls there is an error and this catches it'''
        ad_urls = []
        for possible_ad_url in possible_ad_urls:
            if base_url in possible_ad_url:
                ad_urls.append(possible_ad_url)
        for ad_url in ad_urls:
            east_bay_apartment_info = get_craigslist_info(ad_url)
            east_bay_apartment_info['ad_url'] = ad_url
            all_east_bay_apartments.append(east_bay_apartment_info)
        count += 100
    return all_east_bay_apartments

if __name__ == '__main__':
    #print get_craigslist_info(sys.argv[1])
    print collect_east_bay_apartments()

    
