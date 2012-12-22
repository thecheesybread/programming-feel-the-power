import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

'''this is the wrapper file for project 1. fill these functions out'''


def identity(url):
    return url


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
