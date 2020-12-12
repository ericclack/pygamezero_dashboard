import pgzrun

from lxml import html
import requests
import ssl

WIDTH = 600
HEIGHT = 500

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
page = requests.get('https://www.bbc.co.uk/weather/2654710/today')
tree = html.fromstring(page.content)

# The first H1 is the area
area = tree.xpath('//h1/text()')[0]

# Now get the weather summaries and temperatures...
# We use xpath to identify the right bit of the webpage to grap
#   e.g. the weather summary is in a <div> with class=
#   wr-day__details__weather-type-description
# So to get the correct xpath, look at the HTML, see what element
# contains the info you want, and look for an attribute such as class
# that you can use to identify it.
summaries = tree.xpath('//div[@class="wr-day__details__weather-type-description"]/text()')
temps = tree.xpath('//span[@class="wr-value--temperature--c"]/text()')


def draw():
   screen.clear()
   # Now print out our forecast
   size = 25

   screen.draw.text("Weather forecast for " + area, (10,0))

   counter = 1
   for summary, temp in zip(summaries, temps):
      if counter == 1:
         screen.draw.text("Today: ", (10,size*counter), fontsize=size)
      elif counter == 2:
         screen.draw.text("Tomorrow: ", (10,size*counter), fontsize=size)
         
      screen.draw.text(temp, topright=(size*6,size*counter), fontsize=size, color="orange")
      screen.draw.text(summary, (size*7,size*counter), fontsize=size)
      counter += 1

pgzrun.go()

# On my Mac - use the right version o
#/usr/local/bin/python3 dashboard_gui_pgz.p
