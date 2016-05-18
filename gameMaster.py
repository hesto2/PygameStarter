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
        self.state = C.STATE_IN_PROGRESS
        self.nextDisplay = None
        self.stateContinue = False
        self.events = []
        pygame.key.set_repeat()

    def run(self):
        while 1:
            self.events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                self.events.append(event)

            self.handleState()
            self.display.tick()
            self.display.draw()
            self.CLOCK.tick(conf.FPS)

    def handleState(self):
        if self.state == C.STATE_CHANGE:
            self.display = self.nextDisplay
            self.nextDisplay = None
            self.state = C.STATE_IN_PROGRESS

    def changeDisplay(self,display):
        self.state = C.STATE_CHANGE
        self.nextDisplay = display
