import glob
import pyttsx3
import os

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

a= []
a = filetotext("C:/poems/rsc/*.txt")

str1 = " "

for element in a[0]:
    str1 = str1 + element

print(str1)

engine = pyttsx3.init()
print(engine)
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.7)
print(voices)
engine.setProperty('voice',voices[1].id)
os.chdir("C://poems/rsc")

engine.save_to_file(str1 , 'C://poems/rsc' +'/test'+'.mp3')
engine.runAndWait()