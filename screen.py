import pygame as pg
import os 
from pygame.locals import *
import glob

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
a = filetotext("C:/poems/rsc/*.txt")

class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 25
        self.color = (0,0,0)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 45
        self.timer = 0.0
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
            for text, rect in self.text:
                rect.y -= 1
            
    def render(self, surf):
        for text, rect in self.text:
            surf.blit(text, rect)

screen = pg.display.set_mode((1000,800))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
cred = Credits(screen_rect, a[0])

i=0
running = True

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255, 213, 59))
    cred.update()
    cred.render(screen)
    pg.display.update()
    clock.tick(90)
    i=i+1
    os.chdir("C://poems/screengrab")
    pg.image.save(screen,"screen"+str(i)+".png")
    pg.display.flip()

pg.quit()
