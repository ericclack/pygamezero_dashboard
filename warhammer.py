from lxml import html
import requests
import ssl
import sys

# Make HTTPS links work:
ssl._create_default_https_context = ssl._create_unverified_context

# Get the page
url = 'https://www.warhammer-community.com/2020/11/25/the-flaw-made-manifest-the-death-company-on-the-battlefield/'
page = requests.get(url, headers={
    'Accept': 'text/html, text/plain, text/sgml, text/css, application/xhtml+xml, */*;q=0.01',
    'User-Agent': 'Lynx/2.8.9rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/1.1.1i'
})
print(page.content)
tree = html.fromstring(page.content)

# The first H1 is the area
titles = tree.xpath('//h1/text()')
print(titles)


