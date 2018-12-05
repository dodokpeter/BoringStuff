#! python3
# luckysearch - Opens several Google search results.
# luckysearch -n3 search item

import requests
import sys
import webbrowser
import bs4
import re

print('Googling...')


# read a number of results opened
argIndex = 1
count = 4

if str(sys.argv[1]).startswith('-n'):
    count = int(re.compile(r'(\d+)$').search(sys.argv[1]).group(1))
    argIndex += 1

searchUrl = 'http://google.com/search?q=' + ' '.join(sys.argv[argIndex:])
res = requests.get(searchUrl)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html5lib')

webbrowser.open(searchUrl)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(count, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
