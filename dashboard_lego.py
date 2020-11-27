from lxml import html
import requests
import ssl

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
page = requests.get('https://www.thebrickfan.com/')
tree = html.fromstring(page.content)

print("Lego news stories:\n")

# The news titles are in <H1>, in an <a> element
titles = tree.xpath('//h1/a/text()')
for t in titles:
   print(t)


