import constants as C
import pygame
class Entity:

    def __init__(self,rect,image):
        self.rect = rect
        self.image = image
        self.mouseHover = False
        self.leftMouseDown = False
        self.rightMouseDown = False
        self.id = self.getGuid()

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
        if self.rect.collidepoint(pygame.mouse.get_pos()):
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
