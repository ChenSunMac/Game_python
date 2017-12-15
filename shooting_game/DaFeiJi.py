# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:34:14 2017

@author: Chens
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygame,random
from pygame.locals import *

windowWidth=420
windowHeight=600
cellSize=20

shots=[]#飞行的子弹
enemys=[]#飞行的敌机


def main():
    #初始化
    global shoted
    shoted= 0
    global enemyed
    enemyed = 0
    pygame.init()
    pygame.key.set_repeat(10) #重复响应一个按键
    global screen,guard
    screen=pygame.display.set_mode((windowWidth,windowHeight))
    pygame.display.set_caption("aircraft")
    gamestart()
    FPS=pygame.time.Clock()
    guard=[{'x':windowWidth/2-cellSize/2,'y':windowHeight-cellSize},#中0
           {'x':windowWidth/2-cellSize/2,'y':windowHeight-2*cellSize},#上1
           {'x': windowWidth / 2-cellSize*3/2, 'y': windowHeight - cellSize},#左2
           {'x': windowWidth / 2+cellSize/2, 'y': windowHeight - cellSize}]#右3


    while True:
        screen.fill((0, 0, 0))
        FPS.tick(5)
        gamemedium()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                #飞机左移
                if event.key==K_LEFT and guard[2]['x']>-1:
                    for body in guard:
                        body['x']-=cellSize
                #飞机右移
                if event.key == K_RIGHT and guard[3]['x'] < windowWidth:
                    for body in guard:
                        body['x'] += cellSize
                #发射子弹
                if event.key==K_UP:
                    shoted+=1
                    shot={'x':guard[1]['x'],'y':guard[1]['y']}
                    shots.insert(0,shot)

        #子弹飞行
        if shots != [] :
            for s in shots:
                s['y']-=2*cellSize
            flag=True
            while(flag and shots!=[]):
                flag=False
                if shots[-1]['y']<0:
                    del shots[-1]
                    flag=True

        #产生敌机
        if random.randint(0,1)==0:
            newenemy={'x':cellSize*random.randint(0,windowWidth/cellSize-1),'y':0}
            enemys.insert(0,newenemy)

        if enemys!=[]:
            for enemy in enemys:
                enemy['y'] += 0.5*cellSize #敌机飞行速度
            drawenemys()

        delshots=[]
        delenemys=[]
        for i in range(len(shots)):
            for j in range(len(enemys)):
                if len(shots) != [] and len(enemys) != []:
                    if shots[i]['x']==enemys[j]['x'] and shots[i]['y']<enemys[j]['y']:
                        delshots.insert(0,i)
                        delenemys.insert(0,j)
        for i in delshots:
            del shots[i]
        for j in delenemys:
            del enemys[j]
            enemyed+=1

        if len(enemys) != 0:
            if enemys[len(enemys)-1]['y'] > windowHeight-cellSize:
                gameover()

        drawshots()
        #drawgrid()
        drawguard()
        pygame.display.update()

#绘制网格
def drawgrid():
    for i in range(cellSize,windowWidth,cellSize):
        pygame.draw.line(screen,(255,255,255),(i,0),(i,windowHeight),1)
    for j in range(cellSize,windowHeight,cellSize):
        pygame.draw.line(screen,(255,255,255),(0,j),(windowWidth,j),1)

#绘制自己的战机
def drawguard():
    for body in guard:
        pygame.draw.rect(screen, (255, 255, 255), (body['x'], body['y'], cellSize, cellSize))

#绘制子弹
def drawshots():
    for s in shots:
        pygame.draw.rect(screen, (255, 255, 255), (s['x']+cellSize/3, s['y']+cellSize/4, cellSize / 3, cellSize/2))

#绘制敌机
def drawenemys():
    for e in enemys:
        pygame.draw.rect(screen, (255, 255, 255), (e['x'], e['y'], cellSize, cellSize/2))
        pygame.draw.rect(screen, (255, 255, 255), (e['x']+cellSize/4, e['y']+cellSize/2, cellSize/2, cellSize / 2))

#游戏开始界面
def gamestart():
    #drawgrid()
    fontObj1 = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj1 = fontObj1.render('Aircraft', True, (255,255,255))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (windowWidth/2, windowHeight/3)
    screen.blit(textSurfaceObj1,textRectObj1)

    fontObj2 =pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj2 = fontObj2.render('Developer : JIE', True,(255, 255, 255))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (windowWidth/2, windowHeight*2/3)
    screen.blit(textSurfaceObj2,textRectObj2)

    pygame.display.update()
    flag=True
    while(flag):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    flag=False

#游戏显示界面
def gamemedium():
    fontObj1 = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj1 = fontObj1.render('enemy: %d'%enemyed , True, (255, 255, 0))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (windowWidth-3*cellSize, 2*cellSize)
    screen.blit(textSurfaceObj1, textRectObj1)

    fontObj2 = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj2 = fontObj2.render('shot: %d' % shoted, True, (255, 255, 0))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (2*cellSize, 2*cellSize)
    screen.blit(textSurfaceObj2, textRectObj2)


#游戏结束界面
def gameover():
    #drawgrid()
    fontObj1 = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj1 = fontObj1.render('Game over!', True, (255, 0, 0))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (windowWidth / 2, windowHeight*3 / 8)
    screen.blit(textSurfaceObj1, textRectObj1)

    fontObj2 = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj2 = fontObj2.render('shot: %d'%shoted, True, (255, 255, 255))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (windowWidth / 2, windowHeight * 8 / 16)
    screen.blit(textSurfaceObj2, textRectObj2)


    fontObj3 = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj3 = fontObj3.render('enemy: %d' % enemyed, True, (255, 255, 255))
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (windowWidth / 2, windowHeight * 9 / 16)
    screen.blit(textSurfaceObj3, textRectObj3)

    pygame.display.update()
    flag = True
    while (flag):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    flag = False



if __name__ == '__main__':
    main()