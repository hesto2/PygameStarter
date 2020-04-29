from entities.obstacles.obstacle import Obstacle
from entities.players.player import Player
import pygame
import constants as C
from tools.collisions import *
# from main import entities
'''
Moveable sides : list
Example: [SIDE_TOP] will allow the block to be pushed up

Passable Sides : list
Example: [SIDE_TOP,SIDE_BOTTOM] will allow an object to move freely between top and bottom
'''
class WallStd(Obstacle):
    def __init__(self,image=None,position={"x":0,"y":0},passableSides=None,moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]):
        if image == None:
            image = pygame.image.load('lib/obstacles/wall.jpg').convert()
        rect = image.get_rect()
        Obstacle.__init__(self,rect,image)
        self.keyCode = 'wm'
        self.type = C.TYPE_WALLSTD
        self.rect.left = position['x']
        self.rect.top = position['y']
        self.moveableSides = moveableSides
        self.passableSides = passableSides
        self.velocityY = 0
        self.velocityX = 0
        self.mass = 2

    def tick(self):
        pass

    def onCollision(self,collider,side):
        # if issubclass(type(collider),Player):
        if self.moveableSides != None and side in self.moveableSides:
            self.velocityX = 0
            self.velocityY = 0
            if side == C.SIDE_TOP:
                collider.velocityY = collider.velocityY + self.mass
                if collider.velocityY > 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == C.SIDE_BOTTOM:
                collider.velocityY = collider.velocityY - self.mass
                if collider.velocityY < 0:
                    collider.velocityY = 0
                self.velocityY = collider.velocityY
            elif side == C.SIDE_LEFT:
                collider.velocityX = collider.velocityX + self.mass
                if collider.velocityX > 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX
            elif side == C.SIDE_RIGHT:
                collider.velocityX = collider.velocityX - self.mass
                if collider.velocityX < 0:
                    collider.velocityX = 0
                self.velocityX = collider.velocityX

            self.rect = self.move(collider,side)
        else:
            moveToEdge(self,collider,side)



    def checkCollision(self,target):
        rect = self.rect
        if checkTop(self,target): target.onCollision(self,C.SIDE_TOP)
        elif checkBottom(self,target): target.onCollision(self,C.SIDE_BOTTOM)
        elif checkLeft(self,target): target.onCollision(self,C.SIDE_LEFT)
        elif checkRight(self,target): target.onCollision(self,C.SIDE_RIGHT)

    def move(self,collider,side):
        entities = C.GAME.display.playArea.entities
        for target in entities:
            if target == self or target == collider:
                continue
            self.checkCollision(target)
            self.checkBoundary()

        self.rect = self.rect.move(self.velocityX,self.velocityY)

        if side in [C.SIDE_TOP,C.SIDE_BOTTOM]:
            collider.velocityY = self.velocityY
        else:
            collider.velocityX = self.velocityX
        return self.rect
