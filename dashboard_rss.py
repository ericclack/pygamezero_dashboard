from lxml import html, etree
import requests
import ssl

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page, use etree for RSS feeds, which are XML
page = requests.get('http://feeds.bbci.co.uk/news/world/europe/rss.xml')
tree = etree.fromstring(page.content)

# See the page content -- for debug
#print(page.content)

# Get the item elements, which are the news items
items = tree.xpath('//item')
for i in items:
    title = i.xpath('title/text()')[0]
    description = i.xpath('description/text()')[0]
    # link =
    print("**" + title + "**")
    print(description)
    print()




