import sys, os
from lxml import html
import requests
import ssl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
page = requests.get('https://www.thebrickfan.com/')
tree = html.fromstring(page.content)

# Helper functions
def open_web_page(url):
   print(url)
   if sys.platform == 'darwin':
      os.system("open " + url)
   else:
      os.system("start " + url)

# Build the GUI
app = QApplication(sys.argv)

w = QWidget()
w.resize(500,300)
w.move(300,300)
w.setWindowTitle("Lego News")

# The news titles are in <H2>, in an <a> element
titles = tree.xpath('//h2/a/text()')
links = tree.xpath('//h2/a/@href')

counter = 1
for t, h in zip(titles, links):
   t = QLabel(t, w)
   t.move(80, 10 + counter * 20)

   b = QPushButton('Go', w)
   b.clicked.connect(lambda x, href=h: open_web_page(href))
   b.move(10, 10 + counter * 20)

   counter += 1   

b = QPushButton('Done', w)
b.clicked.connect(app.quit)
b.move(10,12*20)

w.show()

# Run the window
app.exec_()
