# Pygame Zero Dashboard

Scrape information from websites and show things on your own dashboard

Tutorial for Brighton Coder Dojo.

# Set up

Check out this repo onto your computer:

```
git clone https://github.com/ericclack/pygamezero_dashboard.git
```

Install the packages we need:

```
pip3 install --user -r requirements.txt
```

# Test it out

```
python3 dashboard.py
```

# Add your own information

Have a look in the `dashboard.py` file to see how we get weather data
from the BBC website. There are three steps to do this:

1. Use `requests.get(url)` to get the webpage
2. Turn the HTML into a tree structure, which makes it easier to find what we need, using `html.fromstring(page.content)`
3. Use `tree.xpath(path)` to pick out the data we need.

## How to write the XPath

First find the page you want to use in your web browser. Now find the
data you want on the webpage and select it with your mouse. Now you need
to see the HTML source code behind this content...

* In *Chrome*, right click your mouse and choose *Inspect*
* In *Safari* you first need to tick *Show Develop menu in menu bar* on the *Advanced* tab in the *Preferences* window, then you can right click and choose *Inspect Element*
* In *Edge* ???
