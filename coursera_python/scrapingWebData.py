import urllib
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_467357.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")


# Retrive 
tags = soup('span')

spans = [int(tag.contents[0]) for tag in tags]
sum = sum(spans)
print (sum)