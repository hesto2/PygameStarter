from constants import *
from tools.collisions import *
from pygame.locals import *
import pygame
class Player:
    top = False
    bottom = False
    left = False
    right = False

    def __init__(self,rect,inputConf,image,name):
        self.rect = rect
        self.keyUp = inputConf['keyUp']
        self.keyDown = inputConf['keyDown']
        self.keyLeft = inputConf['keyLeft']
        self.keyRight = inputConf['keyRight']
        self.image = image
        self.name = name
        self.velocityX = 0
        self.velocityY = 0
        self.directionX = 1
        self.directionY = 1
        self.maxSpeed = 5


    def move(self,entities,boundary):
        for target in entities:
            if hasattr(target,'name'):
                if target.name == self.name:
                    continue
            self.checkCollision(target)
            self.checkBoundary(boundary)
        self.rect = self.rect.move(self.velocityX,self.velocityY)
        return self.rect

    def onCollision(self,collider,side):
        if issubclass(type(collider),Player):
            moveToEdge(self,collider,side)

# Collision Detection
    def checkBoundary(self,boundary):
        if self.rect.top + self.velocityY < 0: self.velocityY = 0 - self.rect.top
        if self.rect.bottom + self.velocityY > boundary['height']: self.velocityY = boundary['height'] - self.rect.bottom
        if self.rect.left + self.velocityX < 0: self.velocityX = 0 - self.rect.left
        if self.rect.right + self.velocityX > boundary['width'] : self.velocityX = boundary['width'] - self.rect.right

    def checkCollision(self,target):
        rect = self.rect
        # if self.checkTop(target) or self.checkBottom(target): self.velocityY = 0
        # if self.checkLeft(target) or self.checkRight(target): self.velocityX = 0

        if checkTop(self,target): target.onCollision(self,SIDE_TOP)
        if checkBottom(self,target): target.onCollision(self,SIDE_BOTTOM)
        if checkLeft(self,target): target.onCollision(self,SIDE_LEFT)
        if checkRight(self,target): target.onCollision(self,SIDE_RIGHT)

        # top = self.checkTop(target)
        # bottom =  self.checkBottom(target)
        # left =  self.checkLeft(target)
        # right =  self.checkRight(target)
        # if

        # return {"top":top,"bottom":bottom,"left":left,"right":right}


    def onCollision(self,collider,side):
        moveToEdge(self,collider,side)

    def handleInput(self):
        keys = pygame.key.get_pressed()
        if keys[player.keyUp]:
                directionY = -1
        if keys[player.keyDown]:
                directionY = 1
        if keys[player.keyLeft]:
                directionX = -1
        if keys[player.keyRight]:
                directionX = 1



    def tick(self):
        handleInput(self)
        handleState(self)
        move(self)

# if rect.top <= target.bottom and rect.top >= target.top:
#     if (rect.left <= target.right and rect.left >= target.left) or\
#         (rect.right >= target.left and rect.right <= target.right):
#         top = True
# if rect.bottom > target.top and rect.bottom < target.bottom:
#     if (rect.left <= target.right and rect.left >= target.left) or\
#         (rect.right >= target.left and rect.right <= target.right):
#         bottom = True
# if rect.left < target.right and rect.left > target.left:
#     if (rect.bottom >= target.top and rect.bottom <= target.bottom) or\
#         rect.top <= target.bottom and rect.top >= target.top:
#         left = True
# if rect.right > target.left and rect.right < target.right:
#     if (rect.bottom >= target.top and rect.bottom <= target.bottom) or\
#         rect.top <= target.bottom and rect.top >= target.top:
#         right = True
