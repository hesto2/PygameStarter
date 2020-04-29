from entities.obstacles.obstacle import Obstacle
from entities.players.player import Player
import pygame
import constants as C
from tools.collisions import *

class WallSolid(Obstacle):
    def __init__(self,image=None,position={"x":0,"y":0}):
        if image == None:
            image = pygame.image.load('lib/obstacles/wallSolid.png').convert()
        rect = image.get_rect()
        Obstacle.__init__(self,rect,image)
        self.keyCode = 'w'
        self.type = C.TYPE_WALL
        self.rect.left = position['x']
        self.rect.top = position['y']
        self.mass = 2


    def tick(self):
        pass

    def onCollision(self,collider,side):
        moveToEdge(self,collider,side)
