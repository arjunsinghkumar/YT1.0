import pygame as pg
import os 
from pygame.locals import *
import glob
import cv2
import numpy as np
import textwrap

pg.init()

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
a = filetotext("D:/Work/Arjun/YT1.0/rsc/*.txt")

str1 = " "

for element in a[0]:
    str1 = str1 + element

print(str1)



class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 30
        self.color = (0,0,0)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 35
        self.timer = 0
        self.delay = 0
        self.make_surfaces()
        
    def make_text(self,message):
        font = pg.font.Font("OpenSans-Light.ttf", self.size)
        text = font.render(message,True,self.color)
        rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buff_centery) )
        return text,rect
        
    def make_surfaces(self):
        self.text = []
        for i, line in enumerate(self.lst):
            l = self.make_text(line)
            l[1].y += i*self.buff_lines
            self.text.append(l)
            
    def update(self):
        if pg.time.get_ticks()-self.timer > self.delay: 
            self.timer = pg.time.get_ticks()
            lt = len(self.text)
            

            for li in range(0,lt):
                text,rect = self.text[li]
                if(rect.y>-40):
                    rect.y -= 10
                
                if(li == lt-1 and rect.y<-30):
                    print("Break NOW!")
                    pg.quit()
                    exit(0);
                    
            
    def render(self, surf):
        for text, rect in self.text:
            surf.blit(text, rect)    

screen = pg.display.set_mode((1200,1000))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
cred = Credits(screen_rect, str1.split('\n'))

running = True

frameSize = (1200, 1000)


out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
            
    screen.fill((255, 213, 59))
    cred.update()
    cred.render(screen)
    pg.display.update()
    clock.tick(60)
    # print(str(int(clock.get_fps())))
    os.chdir("D:/Work/Arjun/kingversion")
    pg.image.save(screen,"screen"+".png") 
    img = cv2.imread('D:/Work/Arjun/kingversion/screen.png')
    out.write(img)
    os.remove('D:/Work/Arjun/kingversion/screen.png')
    out.write(img)
    pg.display.flip()

pg.quit()

