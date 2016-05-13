import pygame,time,sys
from displays.display import Display
import constants as C
import conf
class GameMaster:
    # Initial Setup of game/screen etc.
    def __init__(self):
        width = 1200
        height = 800
        size = [C.SCREEN_WIDTH,C.SCREEN_HEIGHT]
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(size)
        entities = []
        self.display =  None


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.display.tick()
            self.display.draw()
            self.CLOCK.tick(conf.FPS)
