import sys
from lxml import html
import requests
import ssl

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

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

app = QApplication(sys.argv)

w = QWidget()
w.resize(300,280)
w.move(300,300)
w.setWindowTitle(area)

t = QLabel("Weather for " + area, w)
t.move(10,10)

counter = 1
for summary, temp in zip(summaries[:10], temps[:10]):
   t = QLabel(temp + " " + summary, w)
   t.move(20, 10 + counter * 20)
   counter += 1

b = QPushButton('Done', w)
b.clicked.connect(app.quit)
b.move(10,12*20)

w.show()

# Run the window
app.exec_()

