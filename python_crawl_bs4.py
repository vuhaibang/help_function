import requests
from bs4 import BeautifulSoup


url = "https://brightside.me/wonder-people/20-people-who-suddenly-felt-like-gulliver-in-the-land-of-little-people-798351/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find("title").text
tag_title_images = soup.find_all("div", class_="_2r__xiKDurulGZmkq4_dl")
title_images = []
for i in tag_title_images:
     title_images.append(i.find("h3").text)
tag_link_images = soup.find_all("div", class_="_33VfCtf4r3F3j0M6ixmUuI Z8eATzA_FLU-_naiW5NAW")
link_images = []
for l in tag_link_images:
     if l.find("a", href=True).attrs['href']:
         link = l.find("a", href=True).attrs['href']


import urllib.request
response = urllib.request.Request(url)
with urllib.request.urlopen(response) as response:
   the_page = response.read().decode("utf-8")
   print(the_page)