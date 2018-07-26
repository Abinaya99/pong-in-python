import random
import sys
import pygame
from pygame import *

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Pong by Abinaya')
posball = [0, 0]
ballspeed = [0, 0]
speed1 = 0
speed2 = 0

def start():
    global pos1, pos2, speed1, speed2  
    pos1 = [4, 250]
    pos2 = [694, 250]
    if random.randrange(0, 2) != 0:
        ballstart(False)
    else:
        ballstart(True)

def background(canvas):
    global pos1, pos2, posball, ballspeed

    canvas.fill((0,0,0))
    pygame.draw.circle(canvas, (255, 255, 255), posball, 20, 0)
    pygame.draw.polygon(canvas, (255,140,0), [[pos2[0] - 5, pos2[1] - 35],[pos2[0] - 5, pos2[1] + 35],[pos2[0] + 5, pos2[1] + 35],[pos2[0] + 5, pos2[1] - 35]], 0)
    pygame.draw.polygon(canvas, (255,140,0), [[pos1[0] - 5, pos1[1] - 35],[pos1[0] - 5, pos1[1] + 35],[pos1[0] + 5, pos1[1] + 35],[pos1[0] + 5, pos1[1] - 35]], 0)
    if (pos2[1] > 35 and pos2[1] < 500 - 35) or (pos2[1] == 35 and speed2 > 0) or (pos2[1] == 500 - 35 and speed2 < 0):
    	pos2[1] += speed2

    if (pos1[1] > 35 and pos1[1] < 500 - 35) or (pos1[1] == 35 and speed1 > 0) or (pos1[1] == 500 - 35 and speed1 < 0):
        pos1[1] += speed1

    posball[0] += int(ballspeed[0])
    posball[1] += int(ballspeed[1])

    if (int(posball[0]) <= 20 and int(posball[1]) in range(pos1[1] - 35, pos1[1] + 35, 1)):
    	ballspeed[0] = -ballspeed[0]
    elif int(posball[0]) <= 20:
    	ballstart(True)

    if (int(posball[1]) <= 10) or (int(posball[1]) >= 500 + 1 - 10):
        ballspeed[1] = - ballspeed[1]

    if int(posball[0]) >= 700 + 1 - 20 and int(posball[1]) in range(
            pos2[1] - 35, pos2[1] + 35, 1):
        ballspeed[0] = -ballspeed[0]
        
    elif int(posball[0]) >= 700 + 1 - 20:
        
        ballstart(False)

def ballstart(right):
    global posball, ballspeed
    posball = [350, 250]
    x = random.randrange(2,4)
    y = random.randrange(3, 5)
    if x == False:
        x = -x
    ballspeed = [x, -y]
   

def down(event):
    global speed1, speed2

    if event.key == K_UP:
        speed2 = -7
    elif event.key == K_DOWN:
        speed2 = 7
    elif event.key == K_w:
        speed1 = -7
    elif event.key == K_s:
        speed1 = 7

def up(event):
    global speed1, speed2

    if event.key in (K_w, K_s):
        speed1 = 0
    elif event.key in (K_UP, K_DOWN):
        speed2 = 0

start()
while True:
    background(window)

    for event in pygame.event.get():

        if event.type == KEYUP:
            up(event) 
        elif event.type == KEYDOWN:
           down(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)