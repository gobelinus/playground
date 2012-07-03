# ============================================================ #
# Game description
# How to Play Memory Puzzle
# In the Memory Puzzle game, several icons are covered up by
# white boxes. There are two of each icon. The player can click
# on two boxes to see what icon is behind them. If the icons 
# match, then those boxes remain uncovered. The player wins 
# when all the boxes on the board are uncovered.
# To give the player a hint, the boxes are quickly uncovered
# once at the beginning of the game.
# ============================================================ #

import pygame
import sys

from pygame.locals import *

# lets start with 4 by 4 game
# define piece dimensions
SQUARE_SIZE = 40
GUTTER = 20
ROWS = 4
COLS = 4

#COLORs
GRAY = pygame.Color(80, 80, 80)

def main():
    """
    """
    # lets start game
    # init
    pygame.init()
    
    # calculate window dimensions considering left-right top-bottom gaps
    window_width = COLS * SQUARE_SIZE + (COLS + 1) * GUTTER
    window_height = ROWS * SQUARE_SIZE + (ROWS + 1) * GUTTER

    # set up drawing surface
    display_surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Memory Puzzle')

    bgcolor = GRAY
    display_surface.fill(bgcolor)

    # run the game loop
    while True:
        # listen on events
        for event in pygame.event.get():
            # if quit event, close game, exit the program.. duh
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # update display
        pygame.display.update()

if __name__ == '__main__':
    main()
