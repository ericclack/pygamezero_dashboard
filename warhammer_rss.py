from lxml import html
import requests
import ssl

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
url = 'http://feeds.feedburner.com/alexhardwicke/warhammercommunity'
page = requests.get(url)
tree = html.fromstring(page.content)
#print(page.content)
titles = tree.xpath('//title/text()')

for t in titles:
    print(t)
