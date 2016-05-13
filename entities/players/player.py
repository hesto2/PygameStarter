from constants import *
import constants as C
from tools.collisions import *
from pygame.locals import *
from entities.entity import Entity
import pygame
class Player(Entity):
    top = False
    bottom = False
    left = False
    right = False

    def __init__(self,rect,inputConf,image,boundary,name):
        self.keyUp = inputConf['keyUp']
        self.keyDown = inputConf['keyDown']
        self.keyLeft = inputConf['keyLeft']
        self.keyRight = inputConf['keyRight']
        self.type = C.TYPE_PLAYER
        self.name = name
        self.velocityX = 0
        self.velocityY = 0
        self.directionX = 1
        self.directionY = 1
        self.maxXSpeed = 10
        self.currentXSpeed = 0
        self.maxYSpeed = 8
        self.currentYSpeed = 0
        self.boundary = boundary

        super().__init__(rect,image)


    def move(self,entities,boundary):
        for target in entities:
            if hasattr(target,'name'):
                if target.name == self.name:
                    continue
            self.checkCollision(target,entities,boundary)
            self.checkBoundary(boundary)
        self.rect = self.rect.move(self.velocityX,self.velocityY)
        return self.rect

# Collision Detection
    def checkBoundary(self,boundary):
        if self.rect.top + self.velocityY < 0: self.velocityY = 0 - self.rect.top
        if self.rect.bottom + self.velocityY > boundary['height']: self.velocityY = boundary['height'] - self.rect.bottom
        if self.rect.left + self.velocityX < 0: self.velocityX = 0 - self.rect.left
        if self.rect.right + self.velocityX > boundary['width'] : self.velocityX = boundary['width'] - self.rect.right

    def checkCollision(self,target,entities,boundary):
        rect = self.rect
        # if self.checkTop(target) or self.checkBottom(target): self.velocityY = 0
        # if self.checkLeft(target) or self.checkRight(target): self.velocityX = 0

        if checkTop(self,target): target.onCollision(self,C.SIDE_TOP,entities,boundary)
        elif checkBottom(self,target): target.onCollision(self,C.SIDE_BOTTOM,entities,boundary)
        elif checkLeft(self,target): target.onCollision(self,C.SIDE_LEFT,entities,boundary)
        elif checkRight(self,target): target.onCollision(self,C.SIDE_RIGHT,entities,boundary)

        # top = self.checkTop(target)
        # bottom =  self.checkBottom(target)
        # left =  self.checkLeft(target)
        # right =  self.checkRight(target)
        # if

        # return {"top":top,"bottom":bottom,"left":left,"right":right}


    def onCollision(self,collider,side,entities,boundary):
        moveToEdge(self,collider,side)

    def handleInput(self):
        keys = pygame.key.get_pressed()
        self.currentXSpeed = 0
        self.currentYSpeed = 0
        if keys[self.keyUp]:
                self.directionY = -1
                self.currentYSpeed = self.maxYSpeed
        if keys[self.keyDown]:
                self.directionY = 1
                self.currentYSpeed = self.maxYSpeed
        if keys[self.keyLeft]:
                self.directionX = -1
                self.currentXSpeed = self.maxXSpeed
        if keys[self.keyRight]:
                self.directionX = 1
                self.currentXSpeed = self.maxXSpeed

    def handleState(self):
        self.velocityX = self.currentXSpeed * self.directionX
        self.velocityY = self.currentYSpeed * self.directionY

    def tick(self):
        self.handleInput()
        self.handleState()
        self.move(C.GAME.display.entities,self.boundary)
        return self.rect
