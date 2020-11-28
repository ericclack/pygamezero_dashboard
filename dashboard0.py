from lxml import html
import requests
import ssl

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
page = requests.get('https://www.bbc.co.uk/weather/2654710/today')
tree = html.fromstring(page.content)

# The first H1 is the area
area = tree.xpath('//h1/text()')[0]
print("Weather forecast for " + area + "\n")


