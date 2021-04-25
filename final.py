#initialise libaries
import glob
import numpy as np
import pandas as pd
import re 
import os
import pyttsx3
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import textwrap

#global variables
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
engine.setProperty('voice',voices[1].id)

#Saving poem links 
url = "https://www.familyfriendpoems.com/poems/children/"
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

#Get URLs
def GetURLs(url,req):
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    links = []
    all_links = page_soup.find_all("a")
    for link in all_links:
        links.append(link.get("href"))
    poems_links = []
    for i in range(len(links)):
        if (str(links[i]).startswith("/poem/")):
            poems_links.append(links[i])
    return(poems_links)

listing = GetURLs(url,req)

def clean_text(text):
    pattern = re.compile('<.*?>')
    clean = re.sub(pattern,'',text)
    clean = clean.strip("[]")
    return clean

def AddLineBreak(lst):
    str1 = " "
    for element in lst:
        str1 = str1 + element
    temp = textwrap.dedent(str1)
    return('\n'.join(l for line in str1.splitlines() 
        for l in textwrap.wrap(line, width=50)))

poemss = [] 

def WriteToTextFile(links):
    for i in range(len(links)):
        poems = []
        url = "https://www.familyfriendpoems.com" + str(links[i])
        req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soupy_page = soup(webpage,"html.parser")
        title = soupy_page.title
        summary = soupy_page.h3
        poem = soupy_page(id = "poem-full")
        title = clean_text(str(title))
        summary = clean_text(str(summary))
        summary = AddLineBreak(summary)
        poem = clean_text(str(poem))
        poems = title + poem + summary
        poemss.append(poems)
        os.chdir("C://poems/rsc")
        with open('poem'+str(i)+'.txt', 'w') as filehandle:
            filehandle.writelines(poems)
        engine.save_to_file(poems , 'C://poems/rsc' +'/Poem'+str(i)+'.mp3')
        engine.runAndWait()
    return(poemss)

data = WriteToTextFile(listing)





# File to text 
def filetotext(pathOfFile):
    lineText=[]
    lst = glob.glob(pathOfFile)
    # print(lst)
    for file in lst:
        pom=[]
        myfile = open(file,"r")
        for line in myfile:
            pom.append(line)
        lineText.append(pom)
        myfile.close()
    return(lineText)


