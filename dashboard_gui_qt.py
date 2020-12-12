import sys
from lxml import html
import requests
import ssl

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

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


def main():

   app = QApplication(sys.argv)

   w = QWidget()
   w.resize(250,150)
   w.move(300,300)
   w.setWindowTitle(area)

   b = QPushButton('Done', w)
   b.clicked.connect(app.quit)
   b.move(50,50)
   
   w.show()

   sys.exit(app.exec_())

main()
