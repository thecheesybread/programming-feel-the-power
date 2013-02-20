import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import sys

'''this is the wrapper file for project 1. fill these functions out'''


def identity(word):
    return word


def get_urls(url):
    http = httplib2.Http()
    status, response = http.request(url)
    all_urls = []
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            all_urls.append(url)
    return all_urls


def containsWord(url, word):
    h = httplib2.Http()
    resp, content = h.request("http://reddit.com", "GET")
    print content
    if word in content:
        print True
    else:
        print False

def get_title(html):
    #fill out here
    title = 'title'
    return title


def get_body(html):
    #fill out here
    body = 'body'
    return body


def get_date(html):
    #fill out here
    date = 'date'
    return date

def get_price(html):
    #fill out here
    price = 'price'
    return price

def get_info(url):
    http = httplib2.Http()
    header, html = http.request(url)
    print header
    title = get_title(html)
    body = get_body(html)
    date = get_date(html)
    price = get_price(html)
    info = {'title' : title, 'body' : body, 'date' : date, 'price' : price}
    return info



if __name__ == '__main__':
    print get_info(sys.argv[1])
    
