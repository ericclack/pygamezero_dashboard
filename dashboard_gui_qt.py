import sys, os
from lxml import html
import requests
import ssl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
WEATHER_URL = "https://www.bbc.co.uk/weather/2654710/today"
page = requests.get(WEATHER_URL)
tree = html.fromstring(page.content)

# The first H1 is the area
area = tree.xpath('//h1/text()')[0]

# Now get the weather summaries and temperatures...
summaries = tree.xpath('//div[@class="wr-day__details__weather-type-description"]/text()')
temps = tree.xpath('//span[@class="wr-value--temperature--c"]/text()')

# Helper functions to open URLs

def open_web_page(url):
   if sys.platform == 'darwin':
      os.system("open " + url)
   else:
      os.system("start " + url)

def open_weather_page():
   open_web_page(WEATHER_URL)


# Now build our Graphical User Interface

app = QApplication(sys.argv)

w = QWidget()
w.resize(300,330)
w.move(300,300)
w.setWindowTitle(area)

t = QLabel("Weather for " + area, w)
t.move(10,10)

counter = 1
for summary, temp in zip(summaries[:10], temps[:10]):
   t = QLabel(temp + " " + summary, w)
   t.move(20, 10 + counter * 20)   
   counter += 1

b = QPushButton('Open Weather Page', w)
b.clicked.connect(open_weather_page)
b.move(10,12*20)
   
b = QPushButton('Done', w)
b.clicked.connect(app.quit)
b.move(10,14*20)

w.show()

# Run the window
app.exec_()
