import pygame
import sys

from pygame.locals import *

# init
pygame.init()

# set up drawing surface
display_surface = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Drawing')

#init few colors
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

# fill the surface with bg color
display_surface.fill(WHITE)

#draw a rect
pygame.draw.rect(display_surface, GREEN, (100, 50, 200, 200))

#draw a colored circle
pygame.draw.circle(display_surface, RED, (200, 150), 50, 0)

"""
#lets try to rotate rect
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
"""

# run the game loop
while True:
    #myrect.inflate_ip(10, 10)
    # listen on events
    for event in pygame.event.get():
        # if quit event, close game, exit the program.. duh
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # update display
    pygame.display.update()
    #fpsClock.tick(FPS)
