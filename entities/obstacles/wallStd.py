from entities.obstacles.obstacle import Obstacle
import pygame
from constants import *
class WallStd(Obstacle):
    def __init__(self,image,position={"x":0,"y":0},passableSides=None):
        rect = image.get_rect()
        Obstacle.__init__(self,rect,image)
        self.rect.left = position['x']
        self.rect.top = position['y']
        if passableSides != None:
            pass

    def tick(self):
        pass

    def onCollision(self,collider,side):
        if side == SIDE_TOP:
            collider.velocityY = 0
        elif side == SIDE_BOTTOM:
            collider.velocityY = 0
        elif side == SIDE_LEFT:
            collider.velocityX = 0
        elif side == SIDE_RIGHT:
            collider.velocityX = 0
