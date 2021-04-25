import numpy as np
import pandas as pd
import re 
import os
import pyttsx3
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

#saving poem links 
url = "https://www.familyfriendpoems.com/poems/children/"
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")

links=[]

all_links = page_soup.find_all("a")
for link in all_links:
    links.append(link.get("href"))

poems_links=[]

for i in range(len(links)):
    if (str(links[i]).startswith("/poem/")):
     poems_links.append(links[i])

#voice check
engine = pyttsx3.init()
print(engine)
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
print(voices)
engine.setProperty('voice',voices[1].id)

engine.say("fuck this shit")
engine.runAndWait()

#create a new directory 
#open link
#save title, author, series and poem 
#convert it to mp3 and save
#convert it to text and save 
#go to parent directory

def clean_text(text):
    pattern = re.compile('<.*?>')
    clean = re.sub(pattern,'',text)
    clean = clean.strip("[]")
    return clean
    
poemss = [] 

directory = 'C:/poems'
new = os.path.join(directory,'resource')
os.mkdir(new)

for i in range(len(poems_links)):
    poems = []
    os.chdir(new)
    url = "https://www.familyfriendpoems.com" + str(poems_links[i])
    req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soupy_page = soup(webpage,"html.parser")
    title = soupy_page.title
    summary = soupy_page.h3
    poem = soupy_page(id = "poem-full")
    title = clean_text(str(title))
    summary = clean_text(str(summary))
    poem = clean_text(str(poem))
    poems = title + poem + summary
    engine.save_to_file(poems , new+'/Poem'+str(i)+'.mp3')
    engine.runAndWait()
    with open('poem'+str(i)+'.txt', 'w') as filehandle:
        filehandle.writelines(poems)
    poemss.append(poems)

