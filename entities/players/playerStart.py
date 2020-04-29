from entities.entity import Entity
import pygame
import constants as C
from tools.collisions import *

class PlayerStart(Entity):
    def __init__(self,position={"x":0,"y":0}):
        image = pygame.image.load('lib/players/playerStart.png').convert()
        rect = image.get_rect()
        Entity.__init__(self,rect,image)
        self.keyCode = 'ps'
        self.type = C.TYPE_PLAYER_START
        self.rect.left = position['x']
        self.rect.top = position['y']
        self.mass = 2


    def tick(self):
        if C.GAME.display.gameMode != C.MODE_CREATE:
            self.image.set_alpha(0)
