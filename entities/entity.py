import constants as C
import pygame
from tools.collisions import *
class Entity:

    def __init__(self,rect,image):
        self.rect = rect
        self.image = image.convert()
        self.mouseHover = False
        self.leftMouseDown = False
        self.rightMouseDown = False
        self.id = self.getGuid()
        self.mouseHover = False

    def onCollision(self,collider,side,boundary=None,flags=None):
        pass

    def getGuid(self):
        self.id = C.GUID
        C.GUID = C.GUID + 1

    def onLeftMouseDown(self):
        pass

    def onRightMouseDown(self):
        pass

    def onLeftMouseUp(self):
        pass

    def onRightMouseUp(self):
        pass

    def onMouseHover(self):
        pass

    def tick(self):
        self.checkMouseEvents()

    def checkMouseEvents(self):
        self.mouseHover = False
        collide = False
        if hasattr(self,'abs_pos'):
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if mouseX > self.abs_pos[0] and mouseX < self.abs_pos[0]+self.rect.width and\
               mouseY > self.abs_pos[1] and mouseY < self.abs_pos[1]+self.rect.height:
               collide = True

        else:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                collide = True

        if collide:
            self.mouseHover = True
            self.onMouseHover()
            if pygame.mouse.get_pressed()[0]:
                self.onLeftMouseDown()
            if pygame.mouse.get_pressed()[2]:
                self.onRightMouseDown()

    def checkBoundary(self):
        playArea = C.GAME.display.playArea.rect
        if self.rect.top + self.velocityY < 0: self.velocityY = 0 - self.rect.top
        if self.rect.bottom + self.velocityY > playArea.height: self.velocityY = playArea.height - self.rect.bottom
        if self.rect.left + self.velocityX < 0: self.velocityX = 0 - self.rect.left
        if self.rect.right + self.velocityX > playArea.width : self.velocityX = playArea.width - self.rect.right

    def isInBoundary(self):
        playArea = C.GAME.display.playArea.rect
        if self.rect.top < 0: return False
        if self.rect.bottom > playArea.height: return False
        if self.rect.left < 0: return False
        if self.rect.right > playArea.width : return False
        return True

    def checkCollision(self,target):
        rect = self.rect
        if checkTop(self,target): target.onCollision(self,C.SIDE_TOP)
        elif checkBottom(self,target): target.onCollision(self,C.SIDE_BOTTOM)
        elif checkLeft(self,target): target.onCollision(self,C.SIDE_LEFT)
        elif checkRight(self,target): target.onCollision(self,C.SIDE_RIGHT)
