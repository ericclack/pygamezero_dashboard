#import pgzrun

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

summaries = tree.xpath('//div[@class="wr-day__details__weather-type-description"]/text()')
temps = tree.xpath('//span[@class="wr-value--temperature--c"]/text()')

counter = 0
for summary, temp in zip(summaries, temps):
   if counter == 0:
      print("Today: ", end="")
   elif counter == 1:
      print("Tomorrow: ", end="")
   print(summary, temp)
   counter += 1

#pgzun.go()

