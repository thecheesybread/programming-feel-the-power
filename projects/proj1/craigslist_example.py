import urllib2
url_to_scrape = 'http://sfbay.craigslist.org/zip/'
html = urllib2.urlopen(url_to_scrape)
for line in html:
    if '.html">' in line and 'http://sfbay.craigslist.org/' in line:
        begin_title = line.find('.html">') + len('.html">')
        end_title = line[begin_title:].find('<') + begin_title
        print line[begin_title:end_title]
