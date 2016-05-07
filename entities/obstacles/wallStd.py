from entities.obstacles.obstacle import Obstacle
from entities.players.player import Player
import pygame
from constants import *
from tools.collisions import *
# from main import entities
'''
Moveable sides : list
Example: [SIDE_TOP] will allow the block to be pushed up

Passable Sides : list
Example: [SIDE_TOP,SIDE_BOTTOM] will allow an object to move freely between top and bottom
'''
class WallStd(Obstacle):
    def __init__(self,image,position={"x":0,"y":0},passableSides=None,moveableSides=None):
        rect = image.get_rect()
        Obstacle.__init__(self,rect,image)
        self.type = TYPE_WALLSTD
        self.rect.left = position['x']
        self.rect.top = position['y']
        self.moveableSides = moveableSides
        self.passableSides = passableSides
        self.velocityY = 0
        self.velocityX = 0
        self.mass = 2

    def tick(self):
        pass

    def onCollision(self,collider,side,entities,boundary):
        # if issubclass(type(collider),Player):
        if self.moveableSides != None and side in self.moveableSides:
            self.velocityX = 0
            self.velocityY = 0
            if side == SIDE_TOP:
                collider.velocityY = collider.velocityY + self.mass
                if colliser.velocityY > 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == SIDE_BOTTOM:
                collider.velocityY = collider.velocityY - self.mass
                if collider.velocityY < 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == SIDE_LEFT:
                collider.velocityX = collider.velocityX + self.mass
                if collider.velocityX > 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX
            elif side == SIDE_RIGHT:
                collider.velocityX = collider.velocityX - self.mass
                if collider.velocityX < 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX

            self.rect = self.move(entities,boundary,collider,side)
        else:
            moveToEdge(self,collider,side)



    def checkCollision(self,target,entities,boundary):
        rect = self.rect
        if checkTop(self,target): target.onCollision(self,SIDE_TOP,entities,boundary)
        elif checkBottom(self,target): target.onCollision(self,SIDE_BOTTOM,entities,boundary)
        elif checkLeft(self,target): target.onCollision(self,SIDE_LEFT,entities,boundary)
        elif checkRight(self,target): target.onCollision(self,SIDE_RIGHT,entities,boundary)

    def move(self,entities,boundary,collider,side):
        for target in entities:
            if target == self or target == collider:
                continue
            self.checkCollision(target,entities,boundary)
            self.checkBoundary(boundary)

        self.rect = self.rect.move(self.velocityX,self.velocityY)

        if side in [SIDE_TOP,SIDE_BOTTOM]:
            collider.velocityY = self.velocityY
        else:
            collider.velocityX = self.velocityX
        return self.rect

    def checkBoundary(self,boundary):
        if self.rect.top + self.velocityY < 0: self.velocityY = 0 - self.rect.top
        if self.rect.bottom + self.velocityY > boundary['height']: self.velocityY = boundary['height'] - self.rect.bottom
        if self.rect.left + self.velocityX < 0: self.velocityX = 0 - self.rect.left
        if self.rect.right + self.velocityX > boundary['width'] : self.velocityX = boundary['width'] - self.rect.right
