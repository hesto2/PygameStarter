import pygame,time
from displays.display import Display
from displays.menus.startMenu import StartMenu
class GameMaster:
    # Initial Setup of game/screen etc.
    def __init__(self):
        width = 1200
        height = 800
        size = [width,height]
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(size)
        entities = []
        self.display =  None


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            self.display.draw()
            self.CLOCK.tick(55)
