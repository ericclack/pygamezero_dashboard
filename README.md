# Python Dashboard

Scrape information from websites and show things on your own dashboard.

Tutorial for Brighton Coder Dojo.

What you will learn: 
- Using a real IDE such as Visual Studio Code
- How to install Python libraries
- How go get web content from a URL
- How to pick out info from the page using XPath expressions

Coming soon:
- How to display this content on a dashboard

# Set up

Check out this repo onto your computer:

```
git clone https://github.com/ericclack/python_dashboard.git
```

Install the packages we need:

```
pip3 install --user -r requirements.txt
```

# Test it out

```
python3 dashboard0.py
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

Now the hard bit, you need to see the set of tags and attributes that will identify the information you need. Here's an example...

Let's say you want to display Lego news headlines from this page: https://www.thebrickfan.com/

When you inspect the source code, you see headlines coded like this...

```
<div class="item-details">
     <h1 class="entry-title"><a href="https://www.thebrickfan.com/new-2021-set-teased-for-lego-black-friday-showcase/" rel="bookmark" title="New 2021 Set Teased for LEGO Black Friday Showcase">New 2021 Set Teased for LEGO Black Friday Showcase</a></h1> <div class="meta-info">
     <div class="td-post-author-name"><div class="td-author-by">By</div> <a href="https://www.thebrickfan.com/author/tormentalous/">Allen "Tormentalous" Tran</a><div class="td-author-line"> - </div> </div> <span class="td-post-date"><time class="entry-date updated td-module-date" datetime="2020-11-25T07:11:34+00:00">November 25, 2020</time></span> <div class="td-post-comments"><a href="https://www.thebrickfan.com/new-2021-set-teased-for-lego-black-friday-showcase/#respond"><i class="td-icon-comments"></i>0</a></div> </div>
<div class="td-post-text-content">
     ...
```

So the headline is in an `<a>` tag, which is in an `<h1>` tag. Therefore we can try the XPath:

```
print tree.xpath('//h1/a/text()')
```

The first `//h1` means find all `<h1>` tags wherever they are in the document, and `text()` means get the text inside the tag. 
