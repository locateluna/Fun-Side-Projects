import requests
from bs4 import BeautifulSoup
import re
import pypub

'''
    Description: This script uses BeautifulSoup and pypub to gather all the chapters of a book and puts them into one .epub.
    Challenges: 1) Some challenges faced were dynamically getting the URLs for each chapter, the name of the chapter was in the URL so I needed to filter through the
                    html to collect the correct URLs.
                    Chapter name example: https://mydramanovel.com/love-in-the-clouds/chapter-1-the-elite-hunter/
                2) Collecting just the chapter and chapter title information from the page. I was able to find the dom element and class for each section. One thing
                    that make this difficult is that each line of the chapter was in its own dom element. To counteract this, I was able to get the parent dom element
                    and use the get_text() with a new line delimiter to make the formatting correct.
'''

base_URL = 'https://mydramanovel.com/love-in-the-clouds/'
response = requests.get('https://mydramanovel.com/love-in-the-clouds/')


soup = BeautifulSoup(response.content, 'html.parser')
links = []

for i, link in enumerate(soup.find_all('a')):
    links.append(link.get('href'))

# Filter links to be just the chapter links
filtered_links = [x for x in links if re.search(base_URL, x)]
unique_links = list(dict.fromkeys(filtered_links))
unique_links.remove(base_URL)

epub = pypub.Epub('Love In The Clouds Epub By: Amanda Dattalo')

# Loop through each of the chapters and collect the content of each chapter and add to epub
for i, link in enumerate(unique_links):
    content = BeautifulSoup(requests.get(link).content,'html.parser')
    title = content.find(class_ ='tdb_title').get_text()
    chapter = content.find(class_ ='tdb_single_content').get_text("\n")
    epub_chap = pypub.create_chapter_from_text(chapter, title=title)
    epub.add_chapter(epub_chap)

epub.create('./Love_In_The_Clouds.epub')