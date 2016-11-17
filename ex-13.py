# Ex-15
# Use urllib2 module to get html content from this link:
# http://www.mattmakai.com/links-learning-web-fundamentals.html
# Python has beautifulsoup library to parse html.
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Print all anchor tags, exclude relative links

import urllib2
from bs4 import BeautifulSoup
response = urllib2.urlopen('http://www.mattmakai.com/links-learning-web-fundamentals.html')
html = response.read()
soup = BeautifulSoup(html)
links = soup.find_all('a')
for eachLink in links:
    print eachLink
