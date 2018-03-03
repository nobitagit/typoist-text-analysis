from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = urlopen("https://en.wikipedia.org/wiki/Typewriter")
readHtml = url.read()
url.close()
#
soup = BeautifulSoup(readHtml, 'html.parser')

# content IDs
content_id = "mw-content-text"

content = soup.find(id=content_id)
paragraphs = content.find_all("p")

def isSup(txt):
    return re.match(r'\[.+\]', txt)

ret = []
for paragraph in paragraphs:
    for string in paragraph.strings:
        if not isSup(string):
            ret.append(string)

# Join the strings.
# Curious about why python join is actually a string method I cam across 2 interesting things
# Why join is a string method in Python
# https://stackoverflow.com/a/493831/1446845
# Why joining is faster that concatenating (not only in Python)
# http://www.bernardi.cloud/2012/11/06/python-string-concatenation-vs-list-join/
out_file = " ".join(ret)
# print(soup.prettify()):w

f1 = open('./testfile.txt', 'w+')
f1.write(out_file)
f1.close()









