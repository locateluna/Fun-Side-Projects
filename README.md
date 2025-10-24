## Table of Contents
- [Fun Side Projects](#fun-side-projects)
  - [Love in the Clouds Webscraper](#love-in-the-clouds-webscraper)

# Fun Side Projects
This is a place where I will upload my one off side projects to document my experience.

## Love in the Clouds Webscraper
Description: 

This script uses BeautifulSoup and pypub to gather all the chapters of the ebook Love in the Clouds by: Bai Lu Cheng Shuang and puts them into one .epub. 

Challenges: 
1) Dynamically getting the URLs for each chapter. The name of the chapter was in each of the URLs so I needed to filter through the html to collect the correct URLs.
    Chapter name example: https://mydramanovel.com/love-in-the-clouds/chapter-1-the-elite-hunter/

2) Collecting just the chapter and chapter title information from the page. I was able to find the dom element and class for each section. One thing that make this difficult is that each line of the chapter was in its own dom element. To counteract this, I was able to get the parent dom element and use the get_text() with a new line delimiter between each dom element to make the formatting correct.